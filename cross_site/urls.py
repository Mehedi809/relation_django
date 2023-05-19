from django.urls import path
from . import views

urlpatterns = [
    path('', views.product1, name='product_list'),
    path('<int:pk>/', views.product2, name='product_detail'),
]
