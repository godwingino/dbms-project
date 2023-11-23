from django.urls import path
from . import views

urlpatterns = [
    path('<str:pk>', views.home, name="home"),
    path('products/', views.product),
    path('contact/', views.contact),
    path('login/', views.login, name="login"),
]
