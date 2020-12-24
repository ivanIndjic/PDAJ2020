
from .models import Student,Grade
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','first_name', 'last_name', 'index_num', 'email']

class GradeSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = Grade
        fields = ['id', 'course', 'value', 'student']
