from django.contrib.auth.models import User

from django.db import models

# Create your models here.


class ToDoList(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80, null=False)
    description = models.TextField(null=False)
    createdAt = models.DateField(auto_now_add=True, null=False)
    updatedAt = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
