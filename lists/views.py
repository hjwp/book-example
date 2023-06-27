from django.shortcuts import redirect, render
from lists.models import Item, List


def home_page(request):
    return render(request, "home.html")


def new_list(request):
    nulist = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=nulist)
    return redirect(f"/lists/{nulist.id}/")


def view_list(request, list_id):
    our_list = List.objects.get(id=list_id)
    items = Item.objects.filter(list=our_list)
    return render(request, "list.html", {"items": items})


def add_item(request):
    pass
