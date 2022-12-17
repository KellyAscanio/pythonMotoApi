from .models import Moto
from rest_framework import serializers

class MotoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Moto
        fields = (
            "id",
            "reference",
            "trademark",
            "model",
            "price",
            "image",
            "supplier",
        )