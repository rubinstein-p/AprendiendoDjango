from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

def contacto(request):
        formulario_contacto = FormularioContacto()
        if request.method=='POST':
                formulario_contacto=FormularioContacto(data=request.POST)
                if formulario_contacto.is_valid():
                        nombre = request.POST.get("nombre")
                        email = request.POST.get("email")
                        contenido = request.POST.get("contenido")
                        try:
                                send_mail(
                                        'Prueba',
                                        'Hola, el Sr. %s cuyo email es: %s, envió el siguiente mensaje: \n\n %s' % 
                                        (nombre, email, contenido), settings.EMAIL_HOST_USER,
                                        ['prubinstein@gmail.com'],
                                        fail_silently=False)
                                return redirect("/contacto/?valido")
                        except:
                                return redirect("/contacto/?invalido")
        return render(request,"contactoApp/contacto.html", {'miFormulario':formulario_contacto})