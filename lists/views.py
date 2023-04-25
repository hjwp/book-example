from django.http import HttpResponse


def home_page(request):
    return HttpResponse("<title>To-Do lists</title>")
