from django.contrib import auth
from django.shortcuts import redirect

def login(request):
    user = auth.authenticate(email=request.POST['email'])
    if user:
        auth.login(request, user)
    return redirect('/')

