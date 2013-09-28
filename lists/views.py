from django.shortcuts import redirect, render
from django.views.generic import FormView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.detail import SingleObjectMixin

from lists.forms import ExistingListItemForm, ItemForm
from lists.models import Item, List


class HomePageView(FormView):
    template_name = 'home.html'
    form_class = ItemForm


class NewListView(CreateView, HomePageView):

    def form_valid(self, form):
        list = List.objects.create()
        Item.objects.create(text=form.cleaned_data['text'], list=list)
        return redirect(list)


class ViewAndAddToList(CreateView, SingleObjectMixin):
    template_name = 'list.html'
    model = List
    form_class = ExistingListItemForm

    def get_form(self, form_class):
        self.object = self.get_object()
        if self.request.method == 'POST':
            data={
                'text': self.request.POST['text'],
                'list': self.object.id
            }
        else:
            data = None
        return form_class(data=data)



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
