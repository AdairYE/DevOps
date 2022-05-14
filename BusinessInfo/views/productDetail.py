from django.shortcuts import render, redirect
from BusinessInfo.models import product

# 产品详情页
def detail_product(request,id):
    return render(request, "details/detail.html",{"productID":id})

def detail_product_dashboard(request,id):
    return render(request,"productManage/dashboard.html",{"productID":id})

def detail_product_workorder(request,id):
    return render(request,"productManage/workorder.html",{"productID":id})

def detail_product_wiki(request,id):
    return render(request,"productManage/wiki.html",{"productID":id})

def detail_product_setting(request,id):
    return render(request,"productManage/setting.html",{"productID":id})


