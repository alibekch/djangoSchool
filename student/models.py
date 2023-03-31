from django.db import models
from main.models import School, Subject
from employee.models import Teacher


class Klass(models.Model):
    number = models.IntegerField()
    letter = models.CharField()
    school_year = models.DateField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)


class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    dob = models.DateField
    class_name = models.ForeignKey(Klass, on_delete=models.CASCADE)


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=32)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    start_time = models.DateField()
    end_time = models.DateField()
