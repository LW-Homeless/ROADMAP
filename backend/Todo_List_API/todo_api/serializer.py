from rest_framework import serializers
from .models import ToDoList


class ObtainItemSerializer(serializers.ModelSerializer):
    createdAt = serializers.SerializerMethodField()
    updatedAt = serializers.SerializerMethodField()

    class Meta:
        model = ToDoList
        fields = ['id', 'title', 'description', 'createdAt', 'updatedAt']

    def get_createdAt(self, obj):
        return obj.createdAt.date() if hasattr(obj.createdAt, 'date') else obj.createdAt

    def get_updatedAt(self, obj):
        return obj.updatedAt.date() if hasattr(obj.updatedAt, 'date') else obj.updatedAt


class CreateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['title', 'description']
        read_only_fields = ['user', 'createdAt']


class UpdateItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDoList
        fields = ['title', 'description', 'updatedAt']
        read_only_fields = ['user', 'updatedAt']
