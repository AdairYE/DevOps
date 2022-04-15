from django.contrib import admin
from django.urls import path
from BusinessInfo import views

urlpatterns = [
    path('index/', views.toIndex, name="BusinessInfo_index"),
    path('editProduct/<str:id>/', views.edit_product, name="edit_product"),
    path('editProduct/<str:id>/delete/', views.delete_product, name="delete_product"),
    path('editProduct/<str:id>/index_delete/', views.index_delete_product, name="indexdelete_product"),

    path('project/index/', views.projectIndex, name="project_index"),
    path('editProject/<str:id>/', views.edit_project, name="edit_project"),
    path('editProject/<str:id>/delete/', views.delete_project, name="delete_project"),
    path('editProject/<str:id>/index_delete/', views.index_delete_project, name="indexdelete_project"),
]
