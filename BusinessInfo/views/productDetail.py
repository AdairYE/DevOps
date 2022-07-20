from django.shortcuts import render, redirect
from BusinessInfo.froms.addWiki import addWikiFrom

# 产品详情页
def detail_product(request,id):
    return render(request, "details/detail.html",{"productID":id})

def detail_product_dashboard(request,id):
    return render(request,"productManage/dashboard.html",{"productID":id})

def detail_product_workorder(request,id):
    return render(request,"productManage/workorder.html",{"productID":id})

def detail_product_wiki(request,id):
    if request.method == "GET":
        addWiki = addWikiFrom()
        return render(request, "details/wiki/wiki.html", {"productID":id,"addWiki":addWiki})

def detail_product_setting(request,id):
    return render(request,"productManage/setting.html",{"productID":id})


