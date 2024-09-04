from django.db import models

# Create your models here.
class Visitor(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    
    

    