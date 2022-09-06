
from django.db import models



class Libreria(models.Model):
    name= models.CharField(max_length=40)
    price= models.FloatField()
    description=models.CharField(max_length=80)
    active=models.BooleanField(default=True)
    image = models.ImageField(upload_to = 'articles/', null=True, blank =True)

    def __str__(self):   #para cambiar el object en django 
        return self.name


class Papeleria(models.Model):
    name =models.CharField(max_length=40)
    price =models.FloatField()
    description=models.CharField(max_length= 80)
    active =models.BooleanField(default=True)
    image = models.ImageField(upload_to = 'articles/', null=True, blank =True)

    def __str__(self):
        return self.name



class Artistica(models.Model):
    name= models.CharField(max_length=40)
    price= models.FloatField()
    description=models.CharField(max_length=80)
    active=models.BooleanField(default=True)
    image = models.ImageField(upload_to = 'articles/', null=True, blank =True)

    def __str__(self):
        return self.name