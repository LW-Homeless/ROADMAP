from django.db import models

# Create your models here.


class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    createdAt = models.DateTimeField(auto_now_add=True, null=False)
    updateAt = models.DateTimeField(null=True)
