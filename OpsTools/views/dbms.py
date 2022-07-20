from django.shortcuts import render
from OpsTools.models import dbms,dbHouse

# Create your views here.

def index(request):
    dbInfo = dbms.objects.all().order_by("-id")
    return render(request,"dbms/index.html",{"dbInfo":dbInfo})