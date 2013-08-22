from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html')


def new_list(request):
    list = List.objects.create()
    try:
        Item.objects.create(text=request.POST['item_text'], list=list)
    except ValidationError:
        error_text = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error_text})
    return redirect('/lists/%d/' % (list.id,))


def view_list(request, list_id):
    list = List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        try:
            Item.objects.create(text=request.POST['item_text'], list=list)
            return redirect('/lists/%d/' % (list.id,))
        except ValidationError:
            error = "You can't have an empty list item"

    return render(request, 'list.html', {'list': list, "error": error})
