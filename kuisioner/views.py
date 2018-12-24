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

from .utils import Tool

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

    def get_id_kuestion(self, key, value):
        get_id = Question.objects.get(id=int(key))
        get_id_kategori = Kategori.objects.get(id=int(key))

        return get_id_kategori
    
    def query_save_database(self, *args, **kwargs):

        try:
            survey = Survey(value=int(value), question=object, kategories=object)
        except expression as identifier:
            pass



    def get(self, request, *args, **kwargs):

        kategori_f6 = Question.objects.all()

        dst_lst = []

        for data in kategori_f6:
            val_dict = {}

            val_dict['id_kategori']=data.ketegories_id
            val_dict['value'] = data.id
            val_dict['text'] = data.jawaban
            dst_lst.append(val_dict)
        
        to_json = json.dumps(dst_lst)

        print(to_json)

        cntx = {
            "title": "quiz",
            "question_data":to_json
        }

        return render(self.request, template_name='quiz/quiz.html', context=cntx)

    def post(self, request, *args, **kwargs):

        k = request.POST.get('data', None)

        # print('ini adalah {}'.format(k))

        to_sjson = json.loads(k)

        try:

            for key, value in to_sjson.items():

                if key == '8':
                    print('ini value pertama value > ',value)

                    for k, v in value.items():

                        value_data = v['rating']

                        tool = Tool(value_data, k, key)

                        tool.save_database()
                    
                    del k
                    del v

                elif key == '9':
                    print('ini value kedua valuenya > ',value)
                    
                    for k, v in value.items():

                        value_data = int(v)

                        tool = Tool(value_data, k, key)

                        tool.save_database()

                    del k
                    del v

                elif key == '10':
                    print('ini value ketiga valuenya > ',value)

                    for data in value:

                        value_data = int(data)

                        tool = Tool(value_data, data, key)


                elif key == '11':
                    print('ini value ketiga valuenya kategori 11 > ',value)

                    get_id_kategori = Question.objects.get(ketegories_id=int(key))

                    if value.isdigit():
                        tool = Tool(value, get_id_kategori.id, key)
                        tool.save_database()
                    
                    else:
                        print('not in format')

                
                elif key == '12':
                    print('ini value kategori 12 > ', value)

                    for data_key, data_value in value.items():

                        check_string = bool(str(data_value), str(data_value).strip())

                        if check_string:
                            
                            print(data_value)
                            
                            tool = Tool(data_value, data_key, key)
                            
                            tool.save_database()
                    
                    del data_key
                    del data_value
                
                elif key == '13':
                    print('ini value kategori 13 >', value)

                    for data_key_13, data_value_13 in value.items():

                        tool = Tool(data_value_13, data_key_13, key)
                        
                        tool.save_database()
                
                elif key == '14':
                    print('ini value kategori 14 > ', value)

                    tool = Tool(value, value, key)

                    tool.save_database()
                
                elif key == '15':
                    print('ini value kategori 15 > ', value)

                    for data_15 in value:

                        tool_15 = Tool(data_15, data_15, key)

                        tool_15.save_database()

                    del data_15

                elif key == '16':
                    print('ini value kategori 16 >', value)

                    tool_16 = Tool(value, value, key)

                    tool_16.save_database()

                    del tool_16
                
                elif key == '17':
                    print('ini value kategori 17 >', value)

                    tool_17 = Tool(value, value, key)

                    tool_17.save_database()

                elif key == '18':
                    print('ini value kategori 18', value)

                    for data_key18, data_value18 in value:

                        tool_18 = Tool(data_value18, data_key18, key)

                        tool_18.save_database()

                elif key == '19':
                    print('ini value kategori 19 ', value)

                    value_data_19 = value['76']['Column 1']
                    value_key_question = list(value.keys())[0]

                    tool_19 = Tool(value_data_19, value_key_question, key)

                    tool_19.save_database()
                
                elif key == '20':

                    print('ini value kategori 20 > ', value)

                    tool_20 = Tool(value, value, key)

                    tool_20.save_database()

                elif key == '21':

                    print('ini value kategori 21 ', value)

                    for data_val_21 in value:

                        tool_21 = Tool(data_val_21, data_val_21, key)

                        tool_21.save_database()
                
                elif key == '22':
                    print('ini value kategori 22 ', value)

                    for data_key_22, data_value_22 in value.items():

                        value_data_key_22 = str(data_value_22['Column 1'])

                        tool_22 = Tool(value_data_key_22, data_key_22, key)

                        tool_22.save_database()

                elif key == '23':
                    print('ini value kategori 23', value)

                    for data_key_23, data_value_23 in value.items():

                        value_data_key_23 = str(data_value_23['Column 1'])

                        tool_23 = Tool(value_data_key_23, data_key_23, key)

                        tool_23.save_database()

                else:
                    print('no data')

        except Exception as e:
            print(e)
        
        
        get_data = {
            'is_taken': "succes"
        }
        
        return HttpResponse(get_data)


    



    
