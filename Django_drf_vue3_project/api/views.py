from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers

from api import models

class DepartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Depart
        fields = "__all__"

class DepartView(ModelViewSet):
    queryset = models.Depart.objects.all()
    serializer_class = DepartSerializer


