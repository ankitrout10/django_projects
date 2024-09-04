from django.db import models

# Create your models here.
class Task_Details(models.Model):
    Task_name = models.CharField(max_length=200)
    Task_status = models.BooleanField(default=False)
    