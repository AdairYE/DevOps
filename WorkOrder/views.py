from django.shortcuts import render, redirect
from WorkOrder.models import product
from WorkOrder.froms.addProduct import addProductFrom
from WorkOrder.froms.editProduct import editProductFrom
from django.http import HttpResponseRedirect, JsonResponse




# Create your views here.
def toIndex(request):
    executeInfo = {"status": "true", "msg": None}
    if request.method == "GET":
        productMeta = product._meta.fields
        productData = product.objects.all()
        addProduct = addProductFrom()
        return render(
            request,
            "workorder/index.html",
            {
                "proNameList": productMeta,
                "productData": productData,
                "addProduct": addProduct
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
        return render(request, "workorder/editProduct.html", {"editProduct": editProduct})
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
        return redirect("/WorkOrder/index/")