from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEGHIJKLMNOPQRSTUVWXYS'))
    if request.GET.get('special characters'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 10))
    for i in range(length):
        thepassword += random.choice(characters)


    return render(request, 'generator/password.html', {'password' :thepassword })

def about(request):
    return render(request, 'generator/about.html')
