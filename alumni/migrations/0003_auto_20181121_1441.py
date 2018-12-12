# Generated by Django 2.1.3 on 2018-11-21 14:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0002_auto_20181121_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategori',
            name='kategori_id',
            field=models.CharField(db_column='kategori_number', default=uuid.uuid4, max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(db_column='question_number', default=uuid.uuid4, max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='total',
            name='total',
            field=models.CharField(db_column='total_number', default=uuid.uuid4, max_length=6, unique=True),
        ),
    ]
