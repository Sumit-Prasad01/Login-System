from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'Authentication/index.html')

def signup(request):
    return render(request, "Authentication/signup.html" )

def signin(request):
    return render(request, "Authentication/signin.html" )

def signout(request):
    pass
