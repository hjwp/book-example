from django.db import models

class List(object):
    pass


class Item(models.Model):
    text = models.TextField(default='')

