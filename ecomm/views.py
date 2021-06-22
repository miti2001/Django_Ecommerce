from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from .models import ProductInformation, Feedback
from .forms import FeedbackForm, SignUpForm

# Create your views here.

# def welcome(request):
#     return redirect('login')

def user_logout(request):
    logout(request)
    return redirect('login')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home2')
    else: 
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home2')
            else:
                messages.info(request, 'Username OR Password is incorrect')

        return render(request, 'registration/login.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home2')
    else: 
        if request.method == "POST":
            form = SignUpForm(request.POST)
            #form = UserCreationForm()
            if form.is_valid():
                userObj = form.cleaned_data
                username = userObj['username']
                email = userObj['email']
                password = userObj['password1']
                if not(User.objects.filter(username=username).exists()):
                    user = form.save()
                    user.refresh_from_db()
                    user.save()
                    user = authenticate(username=username, password=password)
                    login(request,user)
                    return redirect('home2')
                else:
                    raise forms.ValidationError('Looks like a username with that email or password already exists')
        else:
            form = SignUpForm()
        return render(request, 'registration/signup.html', {
            'form': form
            })

@login_required(login_url='login')
def feedback(request):
    if request.method == 'GET':
        form = FeedbackForm
        return render(request, 'feedback.html', {
            'form': form,
        })
    elif request.method == 'POST':
        form = FeedbackForm(request.POST)
        #user_email=form.cleaned_data.get['email']
        user_email=form['email'].value()
        print(user_email)
        if form.is_valid():
            form.save()
            return redirect('home2')

@login_required(login_url='login')
def buy_now(request):
    if( request.method == 'GET'):
        id_from_url = request.GET.get('id2')
        content = ProductInformation.objects.filter(id=id_from_url).values()
        #return HttpResponse(content)
        content = content[0]
        name = content['name']
        price = content['price']
        quantity = content['quantity']
        return render(request, 'buy_now.html',{
            'name': name,
            'price': price,
            'quantity': quantity
        })
    
    elif request.method =='POST':
        new_id = request.GET.get('id2')
        content = ProductInformation.objects.filter(id=new_id).values()
        content = content[0]
        name = content['name']
        price = content['price']
        quantity = content['quantity']
        user_required_quantity = request.POST.get('user_quantity')
        if int(user_required_quantity)> int(quantity):
            return HttpResponse('Quantity Exceeded')
        else:
            cont = ProductInformation.objects.get(id=new_id)
            cont.quantity = int(quantity)- int(user_required_quantity)
            cont.save()
            final_price = int(user_required_quantity)*int(price)

            return render(request, 'final_price.html',{
                'final_price': final_price,
            })

@login_required(login_url='login')
def more_info(request):
    id_from_url=request.GET.get('id')
    content = ProductInformation.objects.filter(id=id_from_url).values()
    return render(request, 'more_info.html', {
        'content': content[0]
    })

def view_info(request):
    value=request.GET.get('category')
    content = ProductInformation.objects.filter(category=value).values_list('id','name','price')
    return render(request, 'view_info.html', {
        'content':content
        })

@login_required(login_url='login')
def home(request):
    name="Miti"
    return render(request, 'home.html', {
        'name':name
    })

    # Usually render takes 3 parameters
    # 3rd para is used, if we want to pass values from backend to frontend
