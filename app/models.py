from django.db import models

# Create your models here.
class Student(models.Model):
    objects = None
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)

    def __str__(self):
        return self.fname
