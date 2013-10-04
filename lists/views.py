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


class ViewAndAddToList(SingleObjectMixin, FormView):
    template_name = 'list.html'
    model = List
    form_class = ExistingListItemForm

    def get(self, *args, **kwargs):
        self.object = self.get_object()
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        self.object = self.get_object()
        return super().post(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['list'] = self.object
        return kwargs

    def get_success_url(self):
        return self.object.get_absolute_url()




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
