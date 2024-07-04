from accounts.models import Token, User


class PasswordlessAuthenticationBackend:
    def authenticate(self, request, uid):
        try:
            token = Token.objects.get(uid=uid)
            return User.objects.get(email=token.email)
        except Token.DoesNotExist:
            return None
