from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, HttpResponse
# Create your views here.


from .backend import SettingsBackend
from .forms import MahasiswaForm

from django.contrib.auth import logout
from django.contrib.auth import login as auth_login

class Home(View):

    def get(self, request):

        cntx = {
            'title': "hallo"
        }

        return render(request, template_name='home/home.html', context=cntx)


def login(request):

    form = MahasiswaForm()
    
    settings = SettingsBackend()

    if request.method == 'POST':

        form = MahasiswaForm(request.POST)

        if form.is_valid():
            nim_user = form.cleaned_data["nim"]
            pwd_user = form.cleaned_data["password"]
            
            user = settings.authenticate(request, username=nim_user, password=pwd_user)

            if user is not None:
                auth_login(request, user, backend='alumni.backend.SettingsBackend')

                return redirect('/')

    context = {
        'form': form
    }
    
    return render(request, template_name='alumni/login_new.html', context=context)


def logout_view(request):
    logout(request)

    return HttpResponseRedirect('/users/login/')

