from django.contrib import admin
from django.urls import path
from WorkOrder import views

urlpatterns = [
    path('base/', views.toBase),
]