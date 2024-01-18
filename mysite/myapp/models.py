from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField()

    def __str__(self):
        return self.name
