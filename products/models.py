from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    code = models.IntegerField(unique=True)
    quantity = models.IntegerField()
    is_availible = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " - " + str(self.code)
