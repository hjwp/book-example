from django.shortcuts import redirect, render
from django.views.generic import FormView
from django.views.generic import CreateView
from django.views.generic.edit import ProcessFormView
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.edit import ModelFormMixin
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


class ViewAndAddToList(CreateView):
    template_name = 'list.html'
    form_class = ExistingListItemForm

    def get_list(self):
        return List.objects.get(id=self.kwargs['list_id'])

    def get(self, *args, **kwargs):
        self.list = self.get_list()
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        self.list = self.get_list()
        return super().post(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if 'data' in kwargs:
            kwargs['data'] = kwargs['data'].copy()
            kwargs['data']['list'] = self.list.id
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['list'] = self.list
        return super().get_context_data(**kwargs)




def view_list(request, list_id):
    list = List.objects.get(id=list_id)

    if request.method == 'POST':
        form = ExistingListItemForm(data=request.POST, list=list)
        if form.is_valid():
            form.save()
            return redirect(list)
    else:
        form = ExistingListItemForm()

    return render(request, 'list.html', {'list': list, "form": form})
