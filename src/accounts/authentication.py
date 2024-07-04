from accounts.models import Token, User


class PasswordlessAuthenticationBackend:
    def authenticate(self, request, uid):
        token = Token.objects.get(uid=uid)
        return User.objects.get(email=token.email)
