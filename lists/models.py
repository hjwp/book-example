from django.db import models

class List(models.Model):
    pass

class Item(models.Model):
    text = models.TextField()
    list = models.ForeignKey(List)


    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
