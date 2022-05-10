from django.contrib import admin
from django.urls import path
from BusinessInfo import views

urlpatterns = [
    # 产品
    path('index/', views.toIndex, name="BusinessInfo_index"),
    path('Product/star/', views.star_product, name="star_product"),
    path('Product/cancelStar/', views.cancelStar_product, name="cancelStar_product"),
    path('detailProduct/<str:id>/', views.detail_product, name="detail_product"),

    # 项目
    path('project/index/', views.projectIndex, name="project_index"),
    path('detailProject/<str:id>/', views.detail_project, name="detail_project"),
    path('project/star/', views.star_project, name="star_project"),
    path('project/cancelStar/', views.cancelStar_project, name="cancelStar_project"),
]
