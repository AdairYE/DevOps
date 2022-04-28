from django.shortcuts import render, redirect
from BusinessInfo.models import product
from BusinessInfo.froms.addProduct import addProductFrom
from BusinessInfo.froms.editProduct import editProductFrom
from django.http import HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

# Create your views here.
def toIndex(request):
    executeInfo = {"status": "true", "msg": None}
    if request.method == "GET":
        productData = []
        productInfo = {}

        starProduct = product.objects.filter(star=request.user).order_by('-id')
        productInfo["name"] = "starProduct"
        productInfo["data"] = starProduct
        productData.append(productInfo)

        productInfo["name"] = "user_CreateProduct"
        productInfo["data"] = product.objects.filter(productOwner=request.user).exclude(id__in=starProduct).order_by("-id")
        productData.append(productInfo)

        productInfo["name"] = "user_PartProject"
        productInfo["data"] = product.objects.filter(participator=request.user).exclude(id__in=starProduct).order_by("-id")
        productData.append(productInfo)

        print(productData)
        return render(
            request,
            "productManage/index.html",
            {
                "productData": productData,
            }
        )
    elif request.method == "POST":
        addProduct = addProductFrom(request.POST)
        if addProduct.is_valid():
            addProduct.save()
        else:
            executeInfo["status"] = "false"
            executeInfo["msg"] = addProduct.errors
        return JsonResponse(executeInfo)


def edit_product(request, id):
    executeInfo = {"status": "true", "msg": None}
    obj = product.objects.filter(id=id).first()
    if request.method == "GET":
        editProduct = editProductFrom(instance=obj)
        return render(request, "productManage/editProduct.html", {"editProduct": editProduct})
    elif request.method == "POST":
        editProduct = editProductFrom(request.POST, instance=obj)
        if editProduct.is_valid():
            editProduct.save()
        else:
            executeInfo["status"] = "false"
            executeInfo["msg"] = editProduct.errors
        return JsonResponse(executeInfo)


def delete_product(request, id):
    executeInfo = {"status": "true", "msg": None}
    if request.method == "GET":
        try:
            product.objects.get(id=id).delete()
        except Exception as err:
            executeInfo["status"] = "false"
            executeInfo["msg"] = "产品删除失败：%s", err
        return JsonResponse(executeInfo)

def index_delete_product(request,id):
    if request.method == "GET":
        product.objects.get(id=id).delete()
        return redirect("/BusinessInfo/index/")