from django.shortcuts import render
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
                "addProduct":addProduct
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

def edit_product(request):
    obj = product.objects.filter(id=request.GET["id"]).first()
    editProduct = editProductFrom(instance=obj)
    return render(request,"workorder/editProduct.html",{"editProduct":editProduct})