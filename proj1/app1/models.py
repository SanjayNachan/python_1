from django.db import models

# Create your models here.

class Student(models.Model):
    rn=models.IntegerField()
    name=models.CharField(max_length=50)
    adr=models.CharField(max_length=50)
    fees=models.FloatField()
    city=models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.rn}---{self.name}----{self.adr}----{self.fees}----{self.city}'
    