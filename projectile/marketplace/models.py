from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=30)


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image = models.FileField(blank=False, null=False, upload_to='car')

    def __str__(self):
        return "{} : {}".format(self.car.name,  self.image.name)
