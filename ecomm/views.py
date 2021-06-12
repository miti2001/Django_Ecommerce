from django.shortcuts import render, HttpResponse
from .models import ProductInformation

# Create your views here.

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
        return HttpResponse('Works')



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
    # 3rd para is a dictionary
    #If we want to pass values from backend to frontend
