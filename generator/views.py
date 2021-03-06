import random

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password': 'asdfjasdkjh'})

def password(request):
    testingPassword = ''

    length = int(request.GET.get('length', 12)) # length is the name that is in the url link of password.html page provided by the form.
    # 12 is the default value.

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):

        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):

        characters.extend(list('1234567890'))

    if request.GET.get('special'):

        characters.extend(list('!@#$%^&*()_+'))

    for x in range(length):
        testingPassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':testingPassword})

