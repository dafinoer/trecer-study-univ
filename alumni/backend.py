from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.forms import forms

from .models import Mahasiswa


class SettingsBackend:

    def authenticate(self, request, username=None, password=None):
        #login_valid = (settings.ADMIN_LOGIN == username)
        # pwd_valid = check_password(password, settings.ADMIN_PASSWORD)

        try:
            # user = Mahasiswa.objects.get(nim=username)
            # data = User.objects.get(id=user.user_id)

            data_user = User.objects.get(mahasiswa__nim=username)

            # pwd_valid = check_password(password, data.password)
            if data_user:
                return data_user

        except User.DoesNotExist:
            print("no exist")
            return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None