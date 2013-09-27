from django.shortcuts import redirect, render
from django.views.generic import FormView
from django.views.generic import CreateView

from lists.forms import ExistingListItemForm, ItemForm
from lists.models import Item, List


class HomePageView(FormView):
    template_name = 'home.html'
    form_class = ItemForm


class NewListView(CreateView):
    template_name = 'home.html'
    form_class = ItemForm


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
