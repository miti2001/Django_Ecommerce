from django.shortcuts import render, HttpResponse
from .models import ProductInformation

# Create your views here.

def more_info(request):
    id_from_url=request.GET.get('id')
    content = ProductInformation.objects.filter(id=id_from_url).values_list()
    return HttpResponse(content)

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
