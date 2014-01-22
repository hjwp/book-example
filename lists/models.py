from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models


class List(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    shared_with = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='shared_lists'
    )

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])


    @property
    def name(self):
        return self.item_set.first().text


    @staticmethod
    def create_new(first_item_text, owner=None):
        list_ = List.objects.create(owner=owner)
        Item.objects.create(text=first_item_text, list=list_)
        return list_



class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')


    def __str__(self):
        return self.text

