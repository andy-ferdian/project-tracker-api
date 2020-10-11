from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from pdb import set_trace
from .models import *


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password',
                  'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined']
        read_only_fields = ('last_login', 'date_joined')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data, password=make_password(password))
        user.save()

        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = make_password(validated_data.get('password', instance.password))
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)

        instance.save()

        return instance

class TaskSerializer(serializers.ModelSerializer):
    # board_column = serializers.SerializerMethodField('get_column_name')

    class Meta:
        model = Task
        fields = ('id', 'name', 'description')
    
    # def get_column_name(self, obj):
    #     return obj.board_column.name

class BoardColumnSerializer(serializers.ModelSerializer):
    task = TaskSerializer(many=True, required=False)

    class Meta:
        model = BoardColumn
        fields = ('id', 'name', 'task')
    
    # def get_task_name(self, obj):
    #     return obj.board_column.name


class ProjectSerializer(serializers.ModelSerializer):
    board_column = BoardColumnSerializer(many=True, required=False)

    class Meta:
        model = Project
        fields = ('name', 'board_column')