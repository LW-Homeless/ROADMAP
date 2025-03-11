from django.db import models

# Create your models here.


class Contact(models.Model):
    id_message = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=100)
    contact_mail = models.EmailField(max_length=100)
    contact_subject = models.CharField(max_length=100)
    contact_message = models.TextField()
