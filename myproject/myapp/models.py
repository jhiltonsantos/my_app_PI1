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


class Topping(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    topping = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name


class CPF(models.Model):
    number = models.CharField(max_length=9)


class personPhysical(models.Model):
    name = models.CharField(max_length=50)
    cpf = models.OneToOneField(
        CPF, related_name='pessoa_fisica', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class personMember(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Group(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(personMember, through='Membership')
    
    def __str__(self):
        return self.name
    

class Membership(models.Model):
    person = models.ForeignKey(personMember, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    
    invite_reason = models.CharField(max_length=100)
