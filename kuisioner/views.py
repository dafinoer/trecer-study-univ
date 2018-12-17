from django.shortcuts import render, redirect
from django.views.generic import View
import json
import logging
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


from .forms import MahasiswaForm

from .models import Kategori, Question, Survey

logger = logging.getLogger(__name__)

class NimLogin(View):

    def get(self, request, *args, **kwargs):
        
        context = {
            "title": "home"
        }
        return render(self.request, template_name='home/home.html', context=context)


class Quizioner(LoginRequiredMixin, View):

    login_url = '/users/login'

    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):

        cntx = {
            "title": "quiz",
        }

        return render(self.request, template_name='quiz/quiz.html', context=cntx)

    def post(self, request, *args, **kwargs):

        k = request.POST.get('data', None)

        # print('ini adalah {}'.format(k))

        to_sjson = json.loads(k)

        print(to_sjson)

        try:

            for key, value in to_sjson.items():

                if key == '8':
                    print('ini value pertama value > ',value)
                    for k, v in value.items():

                        value_data = v['rating']
                        
                        get_id = Question.objects.get(id=int(k))

                        get_id_kategori = Kategori.objects.get(id=int(key))

                        # survey = Survey(value=value_data, question=get_id, kategories=get_id_kategori)

                        # survey.save()

                elif key == '9':
                    print('ini value kedua valuenya > ',value)
                    
                    for k, v in value.items():
                        print(k)
                        print(v)

                        get_id = Question.objects.get(id=int(k))

                        get_id_kategori = Kategori.objects.get(id=int(key))

                        try:

                            survey = Survey(value=int(v), question=get_id, kategories=get_id_kategori)
                            survey.save()

                        except ValueError as e:
                            print(e)


                elif key == '10':
                    print('ini value ketiga valuenya > ',value)
                else:
                    print('no data')
                


        except Exception as e:
            print(e)
        
        # try:
        #     for key, value in to_sjson.items():

        #         get_id_question = Question.objects.get(id=int(value))

        #         data = Survey(value=key, question=get_id_question)

        #         data.save()

        # except Exception as e:
        #     print(e)

        
        get_data = {
            'is_taken': "succes"
        }
        
        return HttpResponse(get_data)



    
