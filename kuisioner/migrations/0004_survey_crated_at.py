# Generated by Django 2.1.3 on 2018-12-02 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuisioner', '0003_survey'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='crated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
