from django.shortcuts import render,redirect
from .models import *
from .serializers import *
from rest_framework import viewsets
from datetime import datetime
class OrderView(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class OrderItemView(viewsets.ModelViewSet):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer

def all_order(request):
    order=Order.objects.filter(created_at=datetime.date(datetime.now()))
    return render(request,'order.html',{'order':order})

def order_detail(request,id):
    ordered_items=OrderItem.objects.filter(order=id)
    return render(request,'order_detail.html',{'ordered_items':ordered_items})

def delete_order(request,id):
    order=Order.objects.get(id=id)
    order.delete()
    return redirect('all_order')