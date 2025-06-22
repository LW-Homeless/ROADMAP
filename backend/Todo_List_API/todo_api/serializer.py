from rest_framework import serializers
from .models import ToDoList


class ObtainItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['id', 'title', 'description', 'createdAt', 'updatedAt']


class CreateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['title', 'description']
        read_only_fields = ['user']


class UpdateItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDoList
        fields = ['title', 'description', 'updatedAt']
        read_only_fields = ['user']
