from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import CarImage
from .serializers import CarImageSerializer, CarBasicSerializer, CarDetailsSerializer


class AddCarView(APIView):

    def post(self, request, *args, **kwargs):

        car_serializer = CarBasicSerializer(data=self.request.data)
        if car_serializer.is_valid():
            _car = car_serializer.save()
            for image in self.request.FILES.getlist('images'):
                car_image = CarImageSerializer(
                    data={
                        'car': _car.id,
                        'image': image
                    }
                )
                if car_image.is_valid():
                    car_image.save()
                else:
                    return Response(car_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(car_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(CarDetailsSerializer(_car).data, status=status.HTTP_201_CREATED)
