from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
# Create your views here.
def home_page(request):
    return render(request, 'home.html')
