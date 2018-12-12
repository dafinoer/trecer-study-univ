from django import forms
from alumni.models import Mahasiswa

class MahasiswaForm(forms.Form):

    nim = forms.CharField(label='Nim', max_length=12, required=True)


    def clean_nim(self):
        nim = self.cleaned_data['nim']

        if Mahasiswa.objects.filter(nim=nim).exists() == False:
            print(nim)
            raise forms.ValidationError('error')
        
        return nim