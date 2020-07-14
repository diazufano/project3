from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Client

# Create your views here.
def index(request):
    return render(request, "users/index.html", {"message":'Ufano´s'})

def login(request):
    if request.method == 'POST':
        if request.POST.get("register") == "Register":
            context = {
                "message":'you must register'
            }
            return render(request, "users/register.html", context) 
        else:
            username = request.POST.get("username")
            password = request.POST.get("password")
            try:
                client = Client.objects.get(paswd=password)
            except Client.DoesNotExist:
                raise   Http404("Client does not exist, please register")
            context = {
                "client":client
                }
            return render(request, "users/client.html", context)
    else:
        context = {
            "message": 'Please log in.'
        }
        return render(request, "users/login.html", context)     

def client(request):
    return render(request, "users/client.html", context)

def register(request):
    context = {
        "message":'you must register'
    }
    return render(request, "users/register.html", context)  