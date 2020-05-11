from django.shortcuts import render
from .models import Service 

# Create your views here.

# Se mete la variable de contexto dentro de un diccionario
def services(request):
    services = Service.objects.all()
    return render(request,'services/services.html', {'services': services})