import requests
from django.contrib.auth import get_user_model

PERSONA_VERIFY_URL = 'https://verifier.login.persona.org/verify'
DOMAIN = 'localhost'
User = get_user_model()


class PersonaAuthenticationBackend(object):

    def authenticate(self, assertion):
        response = requests.post(
            PERSONA_VERIFY_URL,
            data={'assertion': assertion, 'audience': DOMAIN}
        )
        if not response.ok:
            return
        if response.json()['status'] == 'okay':
            email = response.json()['email']
            try:
                return self.get_user(email)
            except User.DoesNotExist:
                return User.objects.create(email=email)


    def get_user(self, email):
        return User.objects.get(email=email)
