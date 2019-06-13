from rest_framework import serializers
from .models import (Car, CarImage)

class CarBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

class CarSingleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ['image']
        
class CarDetailsSerializer(serializers.ModelSerializer):
    carimage_set=CarSingleImageSerializer(many=True)
    class Meta:
        model = Car
        fields = ['name','carimage_set']

class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = "__all__"
        
