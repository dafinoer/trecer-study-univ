from django.db import models
import datetime
import uuid
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User, update_last_login

# Create your models here.
class Mahasiswa(models.Model):
    JURUSAN = (
        ('Sistem Informasi', 'Sistem Informasi'),
        ('Teknik Informatika', 'Teknik Informatika'),
        ('Broadcasting', 'Broadcasting')
    )

    YEAR = []
    for data in range(1990, (datetime.datetime.now().year+1)):
        YEAR.append((data, data))

    id = models.AutoField(primary_key=True)
    nim = models.CharField(max_length=12, unique=True, blank=False)
    jurusan = models.CharField(max_length=100, choices=JURUSAN, blank=True)
    tahun_lulus = models.IntegerField(choices=YEAR, blank=True)
    crated_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_column='user_id', null=True)

    class Meta:
        db_table ='mahasiswa'

    def __str__(self):
        return self.nim


