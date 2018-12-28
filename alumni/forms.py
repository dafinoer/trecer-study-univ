from .models import Mahasiswa
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class MahasiswaForm(forms.Form):

    nim = forms.CharField(label='Nim', max_length=12,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Masukan Nim'})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))

    # def clean_nim(self):
    #     nim = self.cleaned_data['nim']
    #
    #     if Mahasiswa.objects.filter(nim=nim).exists() == False:
    #         raise forms.ValidationError('nim not exists')

    def clean(self):

        cleaned_data = super().clean()
        nim_data = cleaned_data.get('nim')
        pwd_data = cleaned_data.get('password')


        if Mahasiswa.objects.filter(nim=nim_data).exists() == False:
            raise forms.ValidationError('nim no exist')

        else:

            nim = Mahasiswa.objects.get(nim=nim_data)
            user = user = User.objects.get(mahasiswa__nim=nim_data)

            pwd_check = check_password(pwd_data, user.password)


            if pwd_check != True:
                raise forms.ValidationError('username n pass salah')