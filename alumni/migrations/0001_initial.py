# Generated by Django 2.1.3 on 2018-11-21 14:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('kategori_id', models.CharField(db_column='kategori_number', default=uuid.uuid4, max_length=6, unique=True)),
                ('tanya', models.TextField(blank=True)),
                ('crated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'kategori',
            },
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nim', models.CharField(max_length=12, unique=True)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('jurusan', models.CharField(blank=True, choices=[('Sistem Informasi', 'Sistem Informasi'), ('Teknik Informatika', 'Teknik Informatika'), ('Broadcasting', 'Broadcasting')], max_length=100)),
                ('tahun_lulus', models.IntegerField(blank=True, choices=[(1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018)])),
                ('crated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'mahasiswa',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(db_column='question_number', default=uuid.uuid4, max_length=6, unique=True)),
                ('jawaban', models.TextField(blank=True)),
                ('crated_at', models.DateTimeField(auto_now_add=True)),
                ('kategori', models.ForeignKey(db_column='kategori_id', on_delete=django.db.models.deletion.CASCADE, to='alumni.Kategori')),
            ],
            options={
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.CharField(db_column='total_number', default=uuid.uuid4, max_length=6, unique=True)),
                ('person_tot', models.IntegerField(blank=True)),
                ('crated_at', models.DateTimeField(auto_now_add=True)),
                ('questions', models.ManyToManyField(db_column='questions_id', to='alumni.Question')),
            ],
            options={
                'db_table': 'total',
            },
        ),
    ]
