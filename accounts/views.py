from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
User = get_user_model()
from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    user = authenticate(assertion=request.POST['assertion'])
    if user:
        auth_login(request, user)
    return HttpResponse('OK')


def my_lists(request, email):
    user = User.objects.get(email=email)
    return render(request, 'my_lists.html', {'owner': user})

