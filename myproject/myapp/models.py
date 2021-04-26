from django.db import models

# Create your models here.

class ToDo(models.Model):
    def __str__ (self):
       return self.name

    name = models.CharField(max_length=100)
    priority = models.IntegerField()
