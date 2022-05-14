from django.contrib import admin
from django.urls import path
from BusinessInfo import views

urlpatterns = [
    # 产品
    path('product/index/', views.toIndex, name="product_index"),

    path('product/star/', views.star_product, name="star_product"),
    path('product/cancelStar/', views.cancelStar_product, name="cancelStar_product"),

    path('product/detail/<str:id>/', views.detail_product, name="detail_product"),
    path('product/detail/<str:id>/dashboard/',views.detail_product_dashboard,name="detail_product_dashboard"),
    path('product/detail/<str:id>/workorder/', views.detail_product_workorder, name="detail_product_workorder"),
    path('product/detail/<str:id>/wiki/', views.detail_product_wiki, name="detail_product_wiki"),
    path('product/detail/<str:id>/setting/', views.detail_product_setting, name="detail_product_setting"),

    # 项目
    path('project/index/', views.projectIndex, name="project_index"),
    path('project/star/', views.star_project, name="star_project"),
    path('project/cancelStar/', views.cancelStar_project, name="cancelStar_project"),
    path('project/detail/<str:id>/', views.detail_project, name="detail_project"),
]
