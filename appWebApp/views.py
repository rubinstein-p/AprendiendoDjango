from django.shortcuts import render, HttpResponse
from carroApp.carro import Carro       

# Create your views here.

def home(request):
        carro=Carro(request)
        return render(request,"appWebApp/home.html")

