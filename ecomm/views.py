from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    name="Miti"
    return render(request, 'home.html', {
        'name':name
    })
    # Usually render takes 3 parameters
    # 3rd para is a dictionary
    #If we want to pass values from backend to frontend
