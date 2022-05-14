from django.shortcuts import render, redirect
from BusinessInfo.models import product
from BusinessInfo.froms.addProduct import addProductFrom
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User


# Create your views here.
def toIndex(request):
    executeInfo = {"status": "true", "msg": None}
    if request.method == "GET":
        addProduct = addProductFrom()
        starProduct = product.objects.filter(star=request.user).order_by('-id')
        productData = {
            "starProduct": starProduct,
            "user_CreateProduct": product.objects.filter(productOwner=request.user).exclude(
                id__in=starProduct).order_by("-id"),
            "user_PartProject": product.objects.filter(participator=request.user).exclude(id__in=starProduct).order_by(
                "-id")
        }

        return render(
            request,
            "productManage/index.html",
            {
                "addProduct": addProduct,
                "productData": productData,
            }
        )

    elif request.method == "POST":
        addProduct = addProductFrom(request.POST)
        if addProduct.is_valid():
            proName = addProduct.save()
            update_author = product.objects.get(name=proName)
            update_author.productOwner = request.user
            update_author.save()
        else:
            executeInfo["status"] = "false"
            executeInfo["msg"] = addProduct.errors
        return JsonResponse(executeInfo)


# 产品标星
def star_product(request):
    executeInfo = {"status": "true", "msg": None}
    if request.method == "GET":
        productID = request.GET["id"]
        username = User.objects.get(username=request.user)
        product.objects.get(id=productID).star.add(username)
        return JsonResponse(executeInfo)

# 取消标星
def cancelStar_product(request):
    executeInfo = {"status": "true", "msg": None}
    if request.method == "GET":
        productID = request.GET["id"]
        username = User.objects.get(username=request.user)
        product.objects.get(id=productID).star.remove(username)
        return JsonResponse(executeInfo)
