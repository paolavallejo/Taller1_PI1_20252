from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # código HTML en views :(
    # return HttpResponse('<h1>Welcome to Home Page</h1>')
    
    #uso de plantilla sin parámetros
    #return render(request, 'home.html')

    # uso de plantilla con parámetros
    return render(request, 'home.html', {'name':'Greg Lim'})

 # Función para 'About'
def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')