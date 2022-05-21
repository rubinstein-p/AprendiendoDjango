from pickle import NONE
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

class VRegistro(View):
    def get(selft, request):
        form=UserCreationForm()
        return render(request,"registro/registro.html",{"form":form})

    def post(self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save() # almacena los datos en la base de datos (crea el usuario)
            login(request,usuario)
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request,"registro/registro.html",{"form":form} )

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def logeo(request):
    if request.method== "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid:
            #nombre_usuario=form.cleaned_data.get("username")
            #contraseña = form.cleaned_data.get("password")
            nombre_usuario = request.POST['username']
            contraseña = request.POST['password'] 
            usuario = authenticate(username=nombre_usuario, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, "Usuario no válido!")
        else:
            messages.error(request, "Usuario no válido!")

    form = AuthenticationForm()
    return render(request,"login/login.html",{"form":form})
