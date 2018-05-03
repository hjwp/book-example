from accounts.models import User

class NoAuthenticationBackend(object):

    def authenticate(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return User.objects.create(email=email)


    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

