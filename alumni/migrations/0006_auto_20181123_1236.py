# Generated by Django 2.1.3 on 2018-11-23 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alumni', '0005_auto_20181121_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='kategori',
        ),
        migrations.RemoveField(
            model_name='total',
            name='questions',
        ),
        migrations.RemoveField(
            model_name='mahasiswa',
            name='name',
        ),
        migrations.AddField(
            model_name='mahasiswa',
            name='user',
            field=models.OneToOneField(db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Kategori',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Total',
        ),
    ]
