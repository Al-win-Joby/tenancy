from django.db import models

# Create your models here.
class Sweettype(models.Model):
    name=models.CharField(max_length=128)

    def __str__(self):
        return self.name