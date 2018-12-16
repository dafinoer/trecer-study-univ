from django.db import models
import datetime
import uuid

# Create your models here.
class Kategori(models.Model):

    id = models.AutoField(primary_key=True)
    kategori_id = models.UUIDField(unique=True, default=uuid.uuid4, db_column='kategori_number')
    tanya = models.TextField(blank=True)
    crated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'kategori'
    
    def __unicode__(self):
        return self.tanya

    def __str__(self):
        return str(self.tanya)


class Question(models.Model):

    id = models.AutoField(primary_key=True)
    question = models.UUIDField(unique=True, default=uuid.uuid4, db_column="question_number", editable=False)
    jawaban = models.TextField(blank=True)
    crated_at = models.DateTimeField(auto_now_add=True)
    # kategories = models.ManyToManyField(Kategori, db_column='kategories_id')
    ketegories = models.ForeignKey(Kategori, on_delete=models.CASCADE, db_column='kategories_id', null=True)

    class Meta:
        db_table = 'question'

    def __str__(self):
        return str(self.question)


class Survey(models.Model):

    id = models.AutoField(primary_key=True)
    value = models.TextField(blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, db_column='question_id')
    kategories = models.ForeignKey(Kategori, on_delete=models.CASCADE, db_column='kuestion_id', default=1)
    crated_at = models.DateTimeField(default=datetime.datetime.now, blank=True)

    class Meta:
        db_table = 'survey'
    
    def __str__(self):
        return str(self.id)