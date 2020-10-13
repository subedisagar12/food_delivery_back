from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
router=DefaultRouter()

router.register('category',views.CategoryView)
router.register('food',views.FoodView)

urlpatterns=[
    path('api/',include(router.urls))
]
