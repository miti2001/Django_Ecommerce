from django.db import models


# Create your models here.

class ProductInformation(models.Model):
    #choices are shown as tuples
    CATEGORY_CHOICES=(
        ('Electronincs','Electronincs'),
        ('Clothing','Clothing'),
        ('Cosmetics','Cosmetics'),
        ('Stationary','Stationary'),
        ('Sports','Sports'),
    )

    name= models.CharField(max_length=32)
    price = models.FloatField()
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES)
    company = models.CharField(max_length=32)
    quantity = models.IntegerField()
    description = models.TextField(blank=True)