from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from OpsTools.models import dbms
from OpsTools.forms.dbms import addDatabaseInfoForm
from django.http import QueryDict

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
    elif request.method == "DELETE":
        # 由于Django对于PUT/DELETE请求并没有像POST/GET那样有一个字典结构。我们需要手动处理request.body获取参数
        DELETE = QueryDict(request.body)
        dbname = DELETE.get("dbname").strip()
        try:
            dbms.objects.get(name=dbname).delete()
            print("[ x ] 删除数据库：",dbname)
        except Exception as e:
            executeInfo["status"] = "false"
            executeInfo["msg"] = e
            return JsonResponse(executeInfo)
        return JsonResponse(executeInfo)

def edit(request,id):
    db_obj = dbms.objects.get(id=id)
    if request.method == "GET":
        DatabaseInfo = addDatabaseInfoForm(instance=db_obj)
        return render(request, "dbms/editDB.html", {"DatabaseInfo": DatabaseInfo,"id":id})
    elif request.method == "POST":
        executeInfo = {"status": "true", "msg": None}
        DatabaseInfo = addDatabaseInfoForm(request.POST,instance=db_obj)
        if DatabaseInfo.is_valid():
            DatabaseInfo.save()
        else:
            executeInfo["status"] = "false"
            executeInfo["msg"] = DatabaseInfo.errors
        return JsonResponse(executeInfo)