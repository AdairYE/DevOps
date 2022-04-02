from django.contrib import admin
from django.urls import path
from WorkOrder import views

urlpatterns = [
    path('index/', views.toIndex,name="workorder_index"),
]