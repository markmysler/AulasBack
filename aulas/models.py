from django.db import models

# Create your models here.

class Aula(models.Model):
    
    name=models.TextField(max_length=255, blank=False, null=False, )
    max_capacity=models.PositiveIntegerField(null=False, blank=False)
    has_negatoscope=models.BooleanField(default=False)

    def __str__(self):
        return self.name