from django.shortcuts import render
from WorkOrder.models import product

# Create your views here.
def toIndex(request):
    if request.method == "GET":
        proNameList = []
        productMeta = product._meta.fields
        for proName in productMeta:
            proNameList.append(proName.verbose_name)
        return render(request,"workorder/index.html",{"proNameList":proNameList})
