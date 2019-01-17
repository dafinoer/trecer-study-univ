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


        cntx = {
            "title": "Tracer Study",
            "question_data":to_json
        }

        return render(self.request, template_name='quiz/quiz.html', context=cntx)

    def post(self, request, *args, **kwargs):

        k = request.POST.get('data', None)

        # print('ini adalah {}'.format(k))

        to_sjson = json.loads(k)

        print('this is json > ',to_sjson)

        try:

            for key, value in to_sjson.items():

                if key == '8':
                    print('ini value pertama value > ',value)

                    for k, v in value.items():

                        value_data = int(v)

                        tool = Tool(value_data, k, key)

                        tool.save_database()
                    
                    del k
                    del v
                
                elif key == '48':
                    print('ini val > ', value)

                    try:
                        get_id_kategories = Question.objects.get(id=key)


                        query_to_survey = Tool(
                                int(value), 
                                key,
                                get_id_kategories.ketegories_id
                            )
                        
                        query_to_survey.save_database()

                    except Exception as identifier:
                        print(identifier)

                    del query_to_survey
                    del get_id_kategories

                elif key == '49':

                    try:
                        ketegories_data = Question.objects.get(id=key)

                        query_data_survey = Tool(
                            int(value),
                            key,
                            ketegories_data.ketegories_id
                        )

                        query_data_survey.save_database()

                    except Exception as identifier:
                        print(identifier)

                    del ketegories_data
                    del query_data_survey

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

                    try:
                        
                        for data in value:
                            
                            value_data = int(data)
                            tool = Tool(value_data, data, key)
                            tool.save_database()

                    except Exception as e:

                        print(e)

                    # for data in value:

                    #     value_data = int(data)

                    #     tool = Tool(value_data, data, key)

                    #     tool.save_database()


                elif key == '11':
                    print('ini value ketiga valuenya kategori 11 > ',value)

                    get_id_kategori = Question.objects.get(ketegories_id=int(key))
                    
                    tool = Tool(value, get_id_kategori.id, key)

                    tool.save_database()
                
                elif key == '12':
                    print('ini value kategori 12 > ', value)

                    for data_key, data_value in value.items():

                        try:
                            tool = Tool(data_value, data_key, key)
                            tool.save_database()
                            print('12 succes save')
                        except Exception as e:
                            print(e)
                        
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

                    for data_key18, data_value18 in value.items():

                        try:
                            tool_18 = Tool(data_value18, data_key18, key)
                            tool_18.save_database()

                            print('18 succes')

                        except Exception as e:

                            print(e)

                        tool_18.save_database()

                elif key == '19':
                    print('ini value kategori 19 ', value)

                    value_data_19 = int(value['76'])

                    value_key_question = list(value.keys())[0]

                    tool_19 = Tool(value_data_19, value_key_question, key)

                    tool_19.save_database()
                
                elif key == '20':

                    print('ini value kategori 20 > ', value)

                    tool_20 = Tool(value, value, key)

                    tool_20.save_database()

                elif key == '21':

                    print('ini value kategori 21 ', value)

                    criteria_user = False

                    data_key_new = 24

                    for data_val_21 in value:

                        if data_val_21 == '81':
                            criteria_user = True
                            print('ini data sesuai pekerjaan> ', data_val_21)
                            break
                        else:
                            print('ini data tidak sesuai pekerjaan> ',data_val_21)
                            break
                    
                    if criteria_user:

                        data_key_value = 126

                        try:
                            tools_21 = Tool(data_key_value, data_key_value, data_key_new)
                            tools_21.save_database()
                            del tools_21
                        except Exception as identifier:
                            print(identifier)

                        del data_key_value

                    else:

                        data_key_value = 127

                        try:
                            tools_21 = Tool(data_key_value, data_key_value, data_key_new)
                            tools_21.save_database()
                            
                            del tools_21

                        except Exception as identifier:
                            print(identifier)
                        
                        del data_key_value

                        # tool_21 = Tool(data_val_21, data_val_21, key)

                        # tool_21.save_database()
                
                elif key == '22':
                    print('ini value kategori 22 ', value)

                    for data_key_22, data_value_22 in value.items():

                        print(data_value_22)

                        try:
                            
                            value_data_key_22 = int(data_value_22)
                            
                            tool_22 = Tool(value_data_key_22, data_key_22, key)

                            tool_22.save_database()

                        except Exception as e:
                            print(e)


                elif key == '23':
                    print('ini value kategori 23', value)

                    for data_key_23, data_value_23 in value.items():


                        try:
                            value_data_key_23 = int(data_value_23)

                            tool_23 = Tool(value_data_key_23, data_key_23, key)

                            tool_23.save_database()

                        except Exception as e:
                            
                            print(e)

                        # tool_23.save_database()
                elif key == '52':
                    print('value 52 ', value)

                    get_kategori_id = Question.objects.get(id=key)

                    try:
                        data_to_int = int(value)
                        survey_input_data = Tool(
                                data_to_int, 
                                key, 
                                get_kategori_id.ketegories_id
                            )
                        survey_input_data.save_database()
                        print('succes 52')
                        
                    except Exception as identifier:
                        print(identifier)

                elif key == '53':
                    print('value 53 ', value)

                    get_id_kategori_id_23 =Question.objects.get(id=key)

                    try:
                        data_convert = int(value)
                        survey_data_23 = Tool(
                            data_convert,
                            key,
                            get_id_kategori_id_23.ketegories_id
                        )

                        survey_data_23.save_database()
                        print('succes 53')
                    except Exception as identifier:
                        print(identifier)

                else:
                    print('no data')

        except Exception as e:
            print('Erorr > ', e)
        
        
        get_data = {
            'is_taken': "succes"
        }
        
        return HttpResponse(get_data)


    



    
