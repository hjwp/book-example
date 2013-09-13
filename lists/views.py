from django.shortcuts import redirect, render

from lists.forms import ExistingListItemForm, ItemForm
from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list = List.objects.create()
        Item.objects.create(text=request.POST['text'], list=list)
        return redirect(list)
    else:
        return render(request, 'home.html', {"form": form})


def view_list(request, list_id):
    list = List.objects.get(id=list_id)

    if request.method == 'POST':
        form = ExistingListItemForm(data={
            'text': request.POST['text'],
            'list': list.id
        })
        if form.is_valid():
            form.save()
            return redirect(list)
    else:
        form = ExistingListItemForm()

    return render(request, 'list.html', {'list': list, "form": form})
