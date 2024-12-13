# serializer.py
from rest_framework import serializers
from .models import Subject, Mcq

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class McqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mcq
        fields = '__all__'
