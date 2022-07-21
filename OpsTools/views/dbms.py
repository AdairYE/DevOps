from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from OpsTools.models import dbms
from OpsTools.forms.dbms import addDatabaseInfoForm

# Create your views here.

def index(request):
    executeInfo = {"status": "true", "msg": None}
    if request.method == "GET":
        addDatabaseInfo = addDatabaseInfoForm()
        dbInfo = dbms.objects.all().order_by("-id")
        return render(request,"dbms/index.html",{"dbInfo":dbInfo,"addDatabaseInfo":addDatabaseInfo})
    elif request.method == "POST":
        addDatabaseInfo = addDatabaseInfoForm(request.POST)
        if addDatabaseInfo.is_valid():
            addDatabaseInfo.save()
        else:
            executeInfo["status"] = "false"
            executeInfo["msg"] = addDatabaseInfo.errors
        return JsonResponse(executeInfo)