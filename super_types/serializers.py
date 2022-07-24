from rest_framework import serializers
from .models import Super_Types

class Super_types_serializers (serializers.ModelSerializer):
    class Meta:
        model = Super_Types
        fields = ['type','id']