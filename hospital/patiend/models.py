from django.db import models

# Create your models here.
class submit(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    disease=models.CharField(max_length=30)