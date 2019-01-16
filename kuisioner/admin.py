from django.contrib import admin
from .models import Kategori, Question, Survey
from django.template.response import TemplateResponse
from django.urls import path
import logging
from django.db import connection
from django.db.models import Q
from django.db.models import Count
import collections


admin.site.site_header = "Admin Page"

logger = logging.getLogger(__name__)

# Register your models here.
@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ('id', 'tanya', 'crated_at')

# admin.site.register(Kategori, KategoriAdmin)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_kuisioner','jawaban', 'crated_at', 'kategori_id')

    search_fields = ('id', 'jawaban', 'ketegories__id')

    def get_kuisioner(self, obj):
        return obj.ketegories.tanya
    
    def kategori_id(self, obj):
        return obj.ketegories.id

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    change_list_template = 'admin/survey.html'
    date_hierarchy = 'crated_at'

    class Media:
        css = {'all':('admin/css/survey.css', )}
        js = (
                'admin/js/Chart.js',
                'admin/js/Chart.min.js', 
                'admin/js/new_chart.js',
            )

    def survey_jawaban(self):
        data = Survey.objects.values_list('value', flat=True)

        try:
            data = self.my_custome_sql()
            logger.debug('ini data ->', data)

        except Exception as e:
            logger.error('ini error -> {} '.format(e))
        
        return data
    
    def my_custome_sql(self):
        
        with connection.cursor() as cursor:
            cursor.execute('''
            select k.tanya, q.jawaban, count(s.question_id)as Count
            from kategori k 
            left join question q on k.id = q.kategories_id
            left join survey s on q.id = s.question_id group by k.id, q.jawaban order by k.id asc
            ''')
            row = cursor.fetchall()
        
        
        return row
    
    def pembelajaran(self):

        get_question_id = Question.objects.filter(ketegories_id=8)

        data_lst = []

        for value_id in get_question_id:

            value_dict = {}
            sangat_buruk_1 = 0
            buruk_2 = 0
            cukup_3 = 0
            baik_4 = 0
            sangat_baik = 0

            query_get_jumlah=Survey.objects.values('value').annotate(
                type_count=Count('value')
                ).filter(question_id=value_id.id).order_by('-type_count')
    

            for data in query_get_jumlah:

                if data['value'] == '5':
                    sangat_baik = data['type_count']
                elif data['value'] == '4':
                    baik_4 = data['type_count']
                elif data['value'] == '3':
                    cukup_3 = data['type_count']
                elif data['value'] == '2':
                    buruk_2 = data['type_count']
                elif data['value'] == '1':
                    sangat_buruk_1 = data['type_count']
                else:
                    print('not found') 
            

            value_dict["tanya"]=value_id.jawaban
            value_dict["sangat_buruk"] = sangat_buruk_1
            value_dict["buruk"] = buruk_2
            value_dict["cukup"] = cukup_3
            value_dict["baik"] = baik_4
            value_dict["sangat_baik"] = sangat_baik
            
            data_lst.append(value_dict)

        print('8 >',data_lst)
        return data_lst
    
    def pencarian_kerja(self):

        get_question_id = Question.objects.filter(ketegories_id=9)

        data_lst = []

        for data in get_question_id:

            value_dict = {}

            get_average = 0

            calculate_avg = 0

            data_avg = []

            try:
                survey_bulan = Survey.objects.filter(question_id=data.id)
                
                data_avg =[int(data.value) for data in survey_bulan]
                
                calculate_avg = collections.Counter(data_avg)

                calculate_avg = get_average / len(data_avg)

                for k in data_avg:
                    get_average +=k

            except Exception as e:
                print(e)



            value_dict['jawaban'] = data.jawaban
            value_dict['average'] = calculate_avg
            value_dict['responden'] = len(data_avg)
            
            data_lst.append(value_dict)

        print('9 > ', data_lst)

        return data_lst
    
    def cara_cari_kerja(self):
        # pertanyaan F3
        get_question_id = Question.objects.filter(ketegories_id=10)

        data_dst=[]

        for data in get_question_id:

            value_dict= {}

            survey_data = Survey.objects.values('value').annotate(
                type_count=Count('value')
            ).filter(question_id=data.id).order_by('-type_count')

            print(survey_data)

            if len(survey_data) != 0:
                value_total = survey_data[0]['type_count']
            else:
                value_total = 0

            value_dict['jawaban'] = data.jawaban
            value_dict['total'] = value_total

            data_dst.append(value_dict)

        print('10 > ', data_dst)
        return data_dst

    def pertanyaan_f6(self):

        question_id = Question.objects.get(ketegories_id=11)

        value_dic = {}

        try:

            data_survey = Survey.objects.filter(question_id=question_id.id)

            collection_value = [int(data.value) for data in data_survey]

            total_avg = sum(collection_value) / len(collection_value)

            value_dic['jawaban'] = question_id.jawaban
            value_dic['average'] = total_avg


        except Exception as identifier:

            print(identifier)


        return value_dic
    
    def pertanyaan_f7(self):

        get_question = Question.objects.filter(ketegories_id=12)

        data_lst = []

        for k in get_question:

            value_dict ={}

            get_average = 0

            data_value = []

            total = 0

            try:
                survey = Survey.objects.filter(question_id=k.id)

                data_value = [int(data.value) for data in survey if len(data.value) != 0]

                total = sum(data_value) / len(data_value)

            except Exception as e:
                print(e)
            

            value_dict['jawaban'] = k.jawaban
            value_dict['average'] = total
            value_dict['total_responden'] = len(data_value)

            data_lst.append(value_dict)
        

        return data_lst

    def pertanyaa_f8(self):
        
        question = Question.objects.filter(ketegories_id=13)

        data_lst = []

        for data in question:

            value_dict = {}

            get_avg = 0

            d_value = []

            total_f8 = 0

            try:
                survey = Survey.objects.filter(question_id=data.id)

                d_value = [int(data.value) for data in survey if data.value.isdigit()]

                total_f8 = sum(d_value) / len(d_value)

            except Exception as e:
                print(e)
                

            value_dict['jawaban'] = data.jawaban
            value_dict['avg'] = total_f8
            value_dict['total_responden'] = len(d_value)
            
            data_lst.append(value_dict)
        

        return data_lst
    
    def pertanyaa_f9(self):

        question = Question.objects.filter(ketegories_id=14)

        data_list = []

        for data in question:
            
            value_dict = {}

            survey = Survey.objects.filter(question_id=data.id).count()

            value_dict['jawaban'] = data.jawaban
            value_dict['total'] = survey

            data_list.append(value_dict)

        print('f9', data_list)

        return data_list
    
    def pertanyaan_10(self):

        question = Question.objects.filter(ketegories_id=15)
        

        data_lst = []

        for data in question:
            value_dict = {}

            survey = Survey.objects.filter(question_id=data.id).count()

            value_dict['jawaban'] = data.jawaban
            value_dict['total'] = survey

            data_lst.append(value_dict)
        


        return data_lst

    
    def pertanyaan_f11(self):
        print('16')

        question = Question.objects.filter(ketegories_id=16)

        data_lst = []

        for data in question:
            value_dict = {}

            survey = Survey.objects.filter(question_id=data.id).count()

            value_dict['jawaban'] = data.jawaban
            value_dict['total'] = survey

            data_lst.append(value_dict)

        print('16 > ', data_lst)

        return data_lst
    
    def pertanyaan_f12(self):
        print('17')

        question = Question.objects.filter(ketegories_id=17)

        data_lst = []

        for data in question:
            value_dict = {}

            survey = Survey.objects.filter(question_id=data.id).count()
            value_dict['jawaban'] = data.jawaban
            value_dict['total'] = survey

            data_lst.append(value_dict)

        print('17 > ',data_lst)

        return data_lst
    
    def pertanyaan_f13(self):
        print('18') 

        question = Question.objects.filter(ketegories_id=18)

        data_lst = []

        tot = 0

        for data in question:
            value_dict = {}

            try:
                survey = Survey.objects.filter(question_id=data.id)
                get_value = [int(k.value) for k in survey]

                tot = sum(get_value)/ len(get_value)

            except Exception as e:
                print(e)

            value_dict['jawaban'] = data.jawaban

            value_dict['avg'] = tot
            data_lst.append(value_dict)          

        print('18 > ',data_lst)
        
        return data_lst
    
    def pertanyaan_f14(self):
        print('19')

        question = Question.objects.filter(ketegories_id=19)

        data_list_value = []

        for data in question:
            value_dict = {}
            
            sangat_buruk_1 = 0
            buruk_2 = 0
            cukup_3 = 0
            baik_4 = 0
            sangat_baik = 0


            try:
                
                query_get_jumlah=Survey.objects.values('value').annotate(
                type_count=Count('value')
                ).filter(question_id=data.id).order_by('-type_count')

                for data_value in query_get_jumlah:
                    if data_value['value'] == '5':
                        sangat_baik = data_value['type_count']
                    elif data_value['value'] == '4':
                        baik_4 = data_value['type_count']
                    elif data_value['value'] == '3':
                        cukup_3 = data_value['type_count']
                    elif data_value['value'] == '2':
                        buruk_2 = data_value['type_count']
                    elif data_value['value'] == '1':
                        sangat_buruk_1 = data_value['type_count']
                    else:
                        print('not found')
                
                value_dict["tanya"]=data.jawaban
                value_dict["sangat_buruk"] = sangat_buruk_1
                value_dict["buruk"] = buruk_2
                value_dict["cukup"] = cukup_3
                value_dict["baik"] = baik_4
                value_dict["sangat_baik"] = sangat_baik

                data_list_value.append(value_dict)

            except Exception as e:
                print(e)

        print('19', data_list_value)

        return data_list_value
    
    def pertanyaan_f15(self):
        print('20')

        question = Question.objects.filter(ketegories_id=20)

        data_lst = []

        try:
            for k in question:
                value_dict = {}

                survey = Survey.objects.filter(question_id=k.id).count()

                value_dict['jawaban'] = k.jawaban
                value_dict['total'] = survey
                data_lst.append(value_dict)

        except Exception as identifier:
            print(identifier)

        print('20 >', data_lst)

        return data_lst
    
    def pertanyaan_f16(self):
        print('21')

        question = Question.objects.filter(ketegories_id=21)

        data_list_value = []

        for k in question:
            value_dict = {}

            survey = Survey.objects.filter(question_id=k.id).count()

            value_dict['jawaban'] = k.jawaban
            value_dict['total'] = survey

            data_list_value.append(value_dict)
        
        print('21 > ', data_list_value)

        return data_list_value
    
    def pertanyaan_f17(self):
        print('22')

        question = Question.objects.filter(ketegories_id=22)

        list_data = []

        for value_17 in question:

            value_dictionary = {}
            
            sangat_baik_data = 0
            baik_data = 0
            cukup_data= 0
            buruk_data= 0
            sangat_buruk_data = 0
 
            try:
                survey = Survey.objects.values('value').annotate(
                    type_count=Count('value')
                    ).filter(question_id=value_17.id).order_by('-type_count')

                print(' 22 > survey ', survey)
                
                for s in survey:
                    if s['value'] == '5':
                        sangat_baik_data = s['type_count']
                    elif s['value'] == '4':
                        baik_data = s['type_count']
                    elif s['value'] == '3':
                        cukup_data = s['type_count']
                    elif s['value'] == '2':
                        buruk_data = s['type_count']
                    elif s['value'] == '1':
                        sangat_buruk_data = s['type_count']
                    else:
                        print(0)
            except Exception as identifier:
                print(identifier)
            
            value_dictionary['jawaban'] = value_17.jawaban
            value_dictionary['sangat_buruk']= sangat_buruk_data
            value_dictionary['buruk'] = buruk_data
            value_dictionary['cukup'] = cukup_data
            value_dictionary['baik'] = baik_data
            value_dictionary['sangat_baik'] = sangat_baik_data

            list_data.append(value_dictionary)
                

        print('22 > ', list_data)

        return list_data
    
    def pertanyaa_f18(self):
        print('23')

        question = Question.objects.filter(ketegories_id=23)

        list_value = []

        for data in question:

            value_dict = {}
            
            sangat_baik_23 = 0
            baik_23 = 0
            cukup_23 = 0
            buruk_23 =0
            sangat_buruk_23 = 0

            try:
                survey = Survey.objects.values('value').annotate(
                    type_count=Count('value')
                ).filter(question_id=data.id).order_by('-type_count')

                for l in survey:

                    if l['value'] == '5':
                        sangat_baik_23 = l['type_count']
                    elif l['value'] == '4':
                        baik_23 = l['type_count']
                    elif l['value'] == '3':
                        cukup_23 = l['type_count']
                    elif l['value'] == '2':
                        buruk_23 = l['type_count']
                    elif l['value'] == '1':
                        sangat_buruk_23 = l['type_count']
                    else:
                        print(0)

            except Exception as identifier:
                print(identifier)
            
            value_dict['jawaban'] = data.jawaban
            value_dict['sangat_baik'] = sangat_baik_23
            value_dict['baik'] = baik_23
            value_dict['cukup'] = cukup_23
            value_dict['buruk'] = buruk_23
            value_dict['sangat_buruk']= sangat_buruk_23

            list_value.append(value_dict)

        print(list_value)

        return list_value
    
    def new_average(self):
        get_question_12 = Question.objects.filter(ketegories_id=12)

        data_lst = []

        for k in get_question_12:

            value_dict ={}

            get_average = 0

            data_value = []

            total = 0

            try:
                survey = Survey.objects.filter(question_id=k.id)

                data_value = [int(data.value) for data in survey if len(data.value) != 0]

                total = sum(data_value) / len(data_value)

            except Exception as e:

                print(e)
            

            # value_dict['jawaban'] = k.jawaban
            # value_dict['average'] = total
            # value_dict['total_responden'] = len(data_value)
            data_new = (k.jawaban, '{} Bulan'.format(int(total)), len(data_value))

            data_lst.append(data_new)
        
        return data_lst

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['survey'] = self.survey_jawaban()
        # extra_context['durasi'] = self.durasi()

        extra_context["pembelajaran"] = self.pembelajaran()
        extra_context['pencarian_kerja'] = self.pencarian_kerja()
        extra_context['cari_kerja'] = self.cara_cari_kerja()
        extra_context['pertanyaan_f6'] = self.pertanyaan_f6()
        extra_context['pertanyaan_f7'] = self.pertanyaan_f7()
        extra_context['pertanyaan_f8'] = self.pertanyaa_f8()
        extra_context['pertanyaa_f9'] = self.pertanyaa_f9()
        extra_context['pertanyaan_10'] = self.pertanyaan_10()
        extra_context['pertanyaan_f11'] = self.pertanyaan_f11()
        extra_context['pertanyaan_f12'] = self.pertanyaan_f12()
        extra_context['pertanyaan_f13'] = self.pertanyaan_f13()
        extra_context['pertanyaan_f14'] = self.pertanyaan_f14()
        extra_context['pertanyaan_f15'] = self.pertanyaan_f15()
        extra_context['pertanyaan_16'] = self.pertanyaan_f16()
        extra_context['pertanyaan_f17'] = self.pertanyaan_f17()
        extra_context['pertanyaa_f18'] = self.pertanyaa_f18()
        extra_context['new_data_average'] = self.new_average()
        

        return super().changelist_view(
            request, extra_context=extra_context
        )
    
    def query_sql(self, id):

        query_sql = '''
            select k.id, k.tanya, q.jawaban, count(s.question_id)as Count
            from kategori k 
            left join question q on k.id = q.kategories_id
            left join survey s on q.id = s.question_id
            where q.kategories_id = {}
            group by k.id, q.jawaban order by k.id asc
            '''.format(id)
        
        return query_sql
    

# class SurveyAdmin(admin.ModelAdmin):
    
#     def get_urls(self):
#         urls = super().get_urls()

#         my_urls = [
#             path('survey_admin/', self.admin_site.admin_view(self.my_view))
#         ]

#         return my_urls + urls

#     def my_view(self, request):

#         context = dict(
#             self.admin_site.each_context(request),
#             key="halo"
#         )

#         return TemplateResponse(request, "admin/survey.html", context)


# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Survey, SurveyAdmin)

