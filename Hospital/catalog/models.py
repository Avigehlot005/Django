from django.db import models

# Create your models here.

class Testing(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.CharField(max_length=100,blank=True,null=True)
    number=models.CharField(max_length=100,blank=True,null=True)
    date=models.DateField(max_length=100,blank=True,null=True)
    message=models.CharField(max_length=500,blank=True,null=True)

def __str__(self):

	return self.name
class Testing2(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True) 
    last=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    subject=models.CharField(max_length=100,blank=True,null=True)
    message=models.CharField(max_length=500,blank=True,null=True)
    def __str__(self):
        return self.name