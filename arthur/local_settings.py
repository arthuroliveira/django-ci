from settings import *

### DEV ZONE AUTH ###
class LocalOverrideBackend(object):
    def authenticate(self, username=None, password=None):
        from django.contrib.auth.models import User
        if password != username: return None
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        return u

    def get_user(self,user_id):
        from django.contrib.auth.models import User
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist: return None


AUTHENTICATION_BACKENDS = list(AUTHENTICATION_BACKENDS) + ["arthur.local_settings.LocalOverrideBackend"]