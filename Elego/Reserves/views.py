from django.http import HttpResponse
from django.shortcuts import render

#from .models import 
# Request: para realizar peticiones
# HttpResponse: Para enviar la respuesta usando el protocolo http

def index(request):
    return HttpResponse("hola mundo. =)")