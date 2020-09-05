from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class ShirtModel(models.Model):
    SHIRT_SIZES = (('P', 'Pequeno'),
                   ('M', 'Medio'),
                   ('G', 'Grande'),
                   )

    name = models.CharField(max_length=50)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


class Fruit(models.Model):
    name = models.CharField(max_length=50, primary_key=True)


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)


class Car(models.Model):
    name = models.CharField(max_length=50)
    manufacter = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name='cars')


