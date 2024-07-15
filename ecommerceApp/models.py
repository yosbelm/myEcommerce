from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(blank=True)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    transaction_id = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.id