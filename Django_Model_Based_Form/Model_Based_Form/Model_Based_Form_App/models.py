from django.db import models

# Create your models here.

class RedgModel(models.Model):
    name=models.CharField(max_length=20)
    dept=models.CharField(max_length=20)
    mark=models.IntegerField()
    apply_course=models.CharField(max_length=20)
    email=models.EmailField()

    