from django.db import models

class User(models.Model):
    email = models.EmailField(primary_key=True)
    REQUIRED_FIELDS = ()
    USERNAME_FIELD = 'email'


    def is_authenticated(self):
        return True



class Token(models.Model):
    pass

