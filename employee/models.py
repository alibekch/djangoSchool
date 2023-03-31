from django.db import models
from main.models import Subject, School


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    date_of_birth = models.DateField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    email = models.CharField()
    phone_number = models.CharField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class Director(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    date_of_birth = models.DateField()
    email = models.CharField()
    phone_number = models.CharField()
    school = models.OneToOneField(School, on_delete=models.CASCADE)


class Deputy(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    date_of_birth = models.DateField()
    email = models.CharField()
    phone_number = models.CharField()
    school = models.OneToOneField(School, on_delete=models.CASCADE)
