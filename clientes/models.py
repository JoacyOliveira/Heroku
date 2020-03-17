from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='produtos')