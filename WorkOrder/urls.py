from django.contrib import admin
from django.urls import path
from WorkOrder import views

urlpatterns = [
    path('index/', views.toIndex,name="workorder_index"),
    path('editProduct/<str:id>/', views.edit_product,name="edit_product"),
    path('editProduct/<str:id>/delete/', views.delete_product,name="delete_product"),
]