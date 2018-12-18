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
    list_display = ('tanya', 'crated_at')

# admin.site.register(Kategori, KategoriAdmin)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_kuisioner','jawaban', 'crated_at')

    def get_kuisioner(self, obj):
        return obj.ketegories.tanya

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    change_list_template = 'admin/survey.html'
    date_hierarchy = 'crated_at'

    class Media:
        css = {'all':('admin/css/survey.css', )}
        js = (
                'admin/js/Chart.js',
                'admin/js/Chart.min.js', 
                'admin/js/chart_bar.js',
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
    
    # def durasi(self):
    #     with connection.cursor() as cursor:
    #        cursor.execute(self.query_sql(1))
    #        data = cursor.fetchall()

    #        print(data)

    #     return data
    
    
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

        # print('print data ',data_lst)

        return data_lst
    
    def pencarian_kerja(self):

        get_question_id = Question.objects.filter(ketegories_id=9)

        data_lst = []

        for data in get_question_id:

            value_dict = {}

            get_average = 0

            survey_bulan = Survey.objects.filter(question_id=data.id)

            data_avg =[int(data.value) for data in survey_bulan]

            calculate_avg = collections.Counter(data_avg)

            for k in data_avg:
                get_average +=k


            calculate_avg = get_average / len(data_avg)


            value_dict['jawaban'] = data.jawaban
            value_dict['average'] = calculate_avg
            value_dict['responden'] = len(data_avg)
            
            data_lst.append(value_dict)


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

        print(data_dst)

        return data_dst


    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['survey'] = self.survey_jawaban()
        # extra_context['durasi'] = self.durasi()

        extra_context["pembelajaran"] = self.pembelajaran()
        extra_context['pencarian_kerja'] = self.pencarian_kerja()
        extra_context['cari_kerja'] = self.cara_cari_kerja()

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

