from django.urls import path
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('process_money', views.procesar),
    path('reset/', views.reset),


]