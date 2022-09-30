from distutils.command.upload import upload
from itertools import product
from statistics import mode
from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

STATE_CHOICES =(  
    ('Andhra Pradesh', 'Andhra Pradesh'), 
    ('Arunachal Pradesh', 'Arunachal Pradesh'), 
    ('Assam', 'Assam'), ('Bihar', 'Bihar'),
    ('Chhattisgar', 'Chhattisgar'), 
    ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), 
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'), 
    ('Karnataka', 'Karnataka'), 
    ('Kerala', 'Kerala'), 
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
    ('Andaman & Nicobar ', 'Andaman & Nicobar '),
    ('Chandigar', 'Chandigar'),
    ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'),
    ('Delh', 'Delh'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Lakshadwee', 'Lakshadwee'),
    ('Puducherr', 'Puducherr'), 
    ('Ladak', 'Ladak')

)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES ,max_length=100)

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES=[
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),
]

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category= models.CharField(choices=CATEGORY_CHOICES ,max_length=5)
    product_image = models.ImageField(upload_to = 'productimg')

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def totalItem_cost(self):
        return self.quantity*self.product.discounted_price


STATUS_CHOICE =[
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Delivered','Delivered'),
    ('Cancle','Cancle')
]

class OrederPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE )
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length= 100 , choices=STATUS_CHOICE ,default='Pending')

    @property
    def totalItem_cost(self):
        return self.quantity*self.product.discounted_price
