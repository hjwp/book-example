from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponse

def login(request):
    user = authenticate(request.POST['assertion'])
    if user:
        auth_login(request, user)
    return HttpResponse('OK')
