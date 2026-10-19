from rest_framework import serializers
from .models import Container, Project

class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
