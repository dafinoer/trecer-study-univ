from django.contrib import admin
from .models import Kategori, Question, Survey
from django.template.response import TemplateResponse
from django.urls import path
import logging
from django.db import connection

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
    
    def durasi(self):
        with connection.cursor() as cursor:
           cursor.execute(self.query_sql(1))
           data = cursor.fetchall()

           print(data)

        return data
    
    def dapat_pekerjaan(self):
        with connection.cursor() as cursor:
            cursor.execute(self.query_sql(2))

            pekerjaan = cursor.fetchall()
            
            print(pekerjaan)

        return pekerjaan
    
    def pekerjaan_pertama(self):
        with connection.cursor() as cursor:
            cursor.execute(self.query_sql(3))

            pertama = cursor.fetchall()

            print(pertama)
        
        return pertama
    
    def penghasilan_pertama(self):
        with connection.cursor() as cursor:
            cursor.execute(self.query_sql(4))

            pnghsilan_pertama = cursor.fetchall()
        
        return pnghsilan_pertama
    
    def sesuai_pekerjaan(self):
        with connection.cursor() as cursor:
            cursor.execute(self.query_sql(5))

            sesuai = cursor.fetchall()
        
        return sesuai
    
    def ipk_kelulusan(self):
        with connection.cursor() as cursor:
            cursor.execute(self.query_sql(7))

            ipk =  cursor.fetchall()
        
        return ipk
    

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['survey'] = self.survey_jawaban()
        extra_context['durasi'] = self.durasi()
        extra_context['pekerjaan'] = self.dapat_pekerjaan()
        extra_context['pertama'] = self.pekerjaan_pertama()
        extra_context['penghasilan'] = self.penghasilan_pertama()
        extra_context['sesuai'] = self.sesuai_pekerjaan()
        extra_context['ipk'] = self.ipk_kelulusan()

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
