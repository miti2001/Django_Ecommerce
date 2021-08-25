from django.db import models
from django.db.models.fields import EmailField
from django.contrib.auth.models import User
#from django.db.models.fields.related import ForeignKey


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return self.name

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

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(ProductInformation, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)


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
