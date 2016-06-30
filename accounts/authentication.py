from accounts.models import User, Token

class PasswordlessAuthenticationBackend(object):

    def authenticate(self, uid):
        token = Token.objects.get(uid=uid)
        return User.objects.get(email=token.email)

