from django import forms
from .forms import FeedbackForm
from django.shortcuts import render, HttpResponse, redirect
from .models import ProductInformation, Feedback
from .forms import FeedbackForm

# Create your views here.
def feedback(request):
    if request.method == 'GET':
        form = FeedbackForm
        return render(request, 'feedback.html', {
            'form': form,
        })
    elif request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home2')

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

def home(request):
    name="Miti"
    return render(request, 'home.html', {
        'name':name
    })

    # Usually render takes 3 parameters
    # 3rd para is used, if we want to pass values from backend to frontend
