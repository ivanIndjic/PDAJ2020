from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    index_num = models.CharField(max_length=10)
    email = models.EmailField()
class Grade(models.Model):
    value = models.PositiveIntegerField(default=10, validators=[MinValueValidator(6),MaxValueValidator(10)])
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)

