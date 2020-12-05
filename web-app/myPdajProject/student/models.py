from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    index_num = models.CharField(max_length=10, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.index_num + ' ' + self.first_name + ' ' + self.last_name + ' ' + self.email
    
class Grade(models.Model):
    value = models.PositiveIntegerField(default=10, validators=[MinValueValidator(5),MaxValueValidator(10)])
    course = models.CharField(max_length=50)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
  
    def __str__(self):
        return str(self.student) + ' ' + str(self.value)
