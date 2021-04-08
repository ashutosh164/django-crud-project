from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12,null=True,blank=True)
    password = models.CharField(max_length=500)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.name