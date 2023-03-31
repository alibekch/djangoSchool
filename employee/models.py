from django.db import models
from main.models import Subject, School


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    date_of_birth = models.DateField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    email = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=120)
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class Director(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=120)
    school = models.OneToOneField(School, on_delete=models.CASCADE)


class Deputy(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=120)
    school = models.OneToOneField(School, on_delete=models.CASCADE)
