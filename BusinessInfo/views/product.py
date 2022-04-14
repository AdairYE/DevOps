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
        productMeta = product._meta.fields
        productData = product.objects.all().order_by("-id")
        addProduct = addProductFrom()

        paginator = Paginator(productData, 10)
        page = request.GET.get('page')
        try:
            productData = paginator.page(page)
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            productData = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            productData = paginator.page(paginator.num_pages)
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            productData = paginator.page(paginator.num_pages)
        return render(
            request,
            "productManage/index.html",
            {
                "proNameList": productMeta,
                "productData": productData,
                "addProduct": addProduct,
                "paginator":paginator
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