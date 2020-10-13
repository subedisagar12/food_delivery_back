from django.db import models
from django.utils import timezone

class Order(models.Model):
    id=models.CharField(max_length=250,primary_key=True)
    client=models.CharField(max_length=200)
    contact=models.CharField(max_length=200)
    email=models.CharField(max_length=200,blank=True)
    address=models.CharField(max_length=200)
    address_description=models.TextField(blank=True)
    created_at=models.DateField(auto_now_add=True)
    order_amount=models.IntegerField()
    isComplete=models.BooleanField(default=False)
    def __str__(self):
        return self.id

class OrderItem(models.Model):
    item=models.CharField(max_length=200)
    qty=models.CharField(max_length=200)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)

    def __str__(self):
        return self.item
