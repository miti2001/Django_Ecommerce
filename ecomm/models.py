from django.db import models
from django.db.models.fields import EmailField


# Create your models here.
class Feedback(models.Model):
    RATING_CHOICES=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )

    name=models.CharField(max_length=64)
    email=models.EmailField() 
    rating=models.CharField(max_length=32, choices=RATING_CHOICES) 
    comments=models.TextField(blank=True)

class ProductInformation(models.Model):
    #choices are shown as tuples
    CATEGORY_CHOICES=(
        ('Electronics','Electronics'),
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

    def __str__(self):
        return self.name + " " + str(self.quantity)