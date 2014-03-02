from django.contrib.auth import authenticate
from django.http import HttpResponse

def persona_login(request):
    authenticate(assertion=request.POST['assertion'])
    return HttpResponse()

