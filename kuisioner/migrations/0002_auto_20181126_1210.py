# Generated by Django 2.1.3 on 2018-11-26 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kuisioner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='kategories',
        ),
        migrations.AddField(
            model_name='question',
            name='ketegories',
            field=models.ForeignKey(db_column='kategories_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='kuisioner.Kategori'),
        ),
    ]
