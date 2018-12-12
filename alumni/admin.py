from django.contrib import admin

from .models import Mahasiswa
from django.contrib.auth.models import User

# Register your models here.
class MahasiswaAuthor(admin.ModelAdmin):
    list_display =('nim', 'jurusan', 'tahun_lulus')

admin.site.register(Mahasiswa, MahasiswaAuthor)