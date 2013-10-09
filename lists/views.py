from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.

def home_page(request):
    return render(request, 'home.html')


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

