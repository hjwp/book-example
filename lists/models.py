from django.db import models


class Item(models.Model):
    text = models.TextField(default="")
