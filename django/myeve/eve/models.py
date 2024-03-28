from django.db import models

# Create your models here.
class Class1(models.Model):
    name=models.CharField(max_length=30)
    stu=models.IntegerField()