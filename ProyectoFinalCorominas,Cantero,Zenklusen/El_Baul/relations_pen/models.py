from django.db import models

# Create your models here.
class Pen_style(models.Model):
    name = models.CharField(max_length=50) 
    
    def __str__(self):    
        return self.name     

class Pen_brand (models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):    
        return self.name     



class Pen (models.Model):
    style = models.ForeignKey(Pen_style, on_delete=models.CASCADE, related_name='style_pen')
    brand = models.ForeignKey(Pen_brand, on_delete=models.CASCADE, null=True,blank=True)
    def __str__(self):    
        return str(self.brand)+"-"+str(self.style)
