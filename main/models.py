from django.db import models
from django.forms import ValidationError
from .utils import validate_phone_number
# school, grade, subject
#  1 Название школы (name)
#  • Адрес школы (address)
#  • Номер телефона школы (phone_number)

#  7 Модель "Предмет" (Subject):
#  • Название предмета (name)
#  • Классы, в которых этот предмет изучается (classes) -- 
#  • Учителя, которые преподают этот предмет (teachers) --

#  8 Модель "Оценка" (Grade):
#  • Ученик, который получил оценку (student)
#  • Учитель, который поставил оценку (teacher)
#  • Предмет, по которому была поставлена оценка (subject)
#  • Класс, в котором получена оценка (class_name) --
#  • Оценка (grade_value)
#  • Дата, когда была поставлена оценка (date)




class School(models.Model):
    
    name = models.CharField(max_length=30, verbose_name='Школа')
    address = models.CharField(max_length=30,  verbose_name='Адрес')
    phone = models.CharField(max_length=15,  
                             verbose_name='Телефон', 
                             unique=True,
                             validators=[validate_phone_number])
    def __str__(self):
        return self.name
    

class Subject(models.Model):
    name = models.CharField(max_length=30, verbose_name='Предмет')
    
    def __str__(self):
        return self.name

class Grade(models.Model):
    name = models.CharField(max_length=30, verbose_name='Оценка')
    student: Student =models.ForeignKey(Student, on_delete=models.PROTECT, related_name='Ученик')
    teacher: Teacher =models.ForeignKey(Teacher , on_delete=models.PROTECT, related_name='Учитель')
    grade_value = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name




