from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
    services = Service.objects.all() #lista de todos los servicios
    return render(request, "services/services.html", {'services':services})