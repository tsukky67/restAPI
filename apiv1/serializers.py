from rest_framework import serializers
from .models import Works

class WorksDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = '__all__'