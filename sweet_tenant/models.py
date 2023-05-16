from django.db import models

from sweet_shared.models import Sweettype
# Create your models here.
class Sweet(models.Model):
    sweet_type = models.ForeignKey(Sweettype,on_delete=models.CASCADE)
    name       = models.CharField(max_length=128)