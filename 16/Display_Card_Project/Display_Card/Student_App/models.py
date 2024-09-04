from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    reg_no=models.IntegerField()
    email=models.EmailField()
    mark=models.IntegerField()
    course=models.CharField(max_length=40)
    college=models.CharField(max_length=26)

    