from django.db import models


# from .models import Category
from django.contrib.auth.models import User



GENDER=[
    ('male','male'),
    ('female','female')
]
# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=50)   
    gender=models.CharField(max_length=10,choices=GENDER)
    address=models.TextField(max_length=300)
    phone=models.CharField(max_length=10)
    def __str__(self) :
        return "Name :"+self.name


class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    # category=models.ForeignKey(Category)
    description=models.TextField(max_length=500)
    image=models.ImageField(upload_to='upload/static/img/')
    def __str__(self):
        return self.name

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'






class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'

    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped')
    )

    user = models.ForeignKey(User, related_name='orders', blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)


    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    paid_amount = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)
    def __str__(self):
        return self.first_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)