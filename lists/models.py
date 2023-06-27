from django.db import models


class List:
    pass


class Item(models.Model):
    text = models.TextField(default="")
