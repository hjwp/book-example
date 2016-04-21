from django.http import HttpResponse

def list(request, list_id):
    return HttpResponse(content_type='application/json')
