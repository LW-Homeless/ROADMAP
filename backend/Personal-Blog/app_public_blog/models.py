from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.


class Contact(models.Model):
    id_message = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=80, null=False)
    contact_email = models.EmailField(max_length=80, null=False)
    contact_suject = models.CharField(max_length=100, null=False)
    contact_message = models.TextField(max_length=5000, null=False)


class Article(models.Model):
    id_article = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=100)
    article_date = models.DateTimeField()
    article_description = models.CharField(max_length=100)
    article_content = CKEditor5Field(config_name='extends')


