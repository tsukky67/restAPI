from django.shortcuts import render
from rest_framework import viewsets
from .models import Works
from .serializers import WorksDataSerializer

class WorksDataViewSet(viewsets.ModelViewSet):
    queryset = Works.objects.all()
    serializer_class = WorksDataSerializer