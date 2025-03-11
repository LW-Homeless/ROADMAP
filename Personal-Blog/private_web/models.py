from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.


class Article(models.Model):
    id_article = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    publishing_date = models.DateTimeField()
    content = CKEditor5Field('Text', config_name='extends')
