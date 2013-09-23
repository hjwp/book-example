from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['item_text'])
    return render(request, 'home.html')
