from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
router=DefaultRouter()
router.register('order',views.OrderView)
router.register('order_item',views.OrderItemView)

urlpatterns=[
    path('',include(router.urls)),
    path('all_order',views.all_order,name="all_order"),
    path('order_detail/<str:id>',views.order_detail,name="order_detail"),
     path('order_detail/<str:id>/delete',views.delete_order,name="delete_order")
]
