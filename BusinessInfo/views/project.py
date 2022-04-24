"""
    项目管理-视图
"""
from django.shortcuts import render,redirect
from BusinessInfo.models import project
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from BusinessInfo.froms.addProject import addProjectFrom
from BusinessInfo.froms.editProject import editProjectFrom
from django.http import JsonResponse

def projectIndex(request):
    executeInfo = {"status": "true", "msg": None}
    if request.method == "GET":
        projectMeta = project._meta.fields
        projectData = project.objects.all().order_by("-id")
        addproject = addProjectFrom()

        paginator = Paginator(projectData, 10)
        page = request.GET.get('page')
        try:
            projectData = paginator.page(page)
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            projectData = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            projectData = paginator.page(paginator.num_pages)
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            projectData = paginator.page(paginator.num_pages)
        return render(
            request,
            "projectManage/index.html",
            {
                "proNameList": projectMeta,
                "projectData": projectData,
                "addproject": addproject,
                "paginator":paginator
            }
        )
    elif request.method == "POST":
        request.POST._mutable = True
        request.POST["author"] = request.user.id
        addproject = addProjectFrom(request.POST)
        request.POST._mutable = False
        print(request.POST)
        if addproject.is_valid():
            addproject.save()
        else:
            executeInfo["status"] = "false"
            executeInfo["msg"] = addproject.errors
        return JsonResponse(executeInfo)

def edit_project(request,id):
    executeInfo = {"status": "true", "msg": None}
    obj = project.objects.filter(id=id).first()
    if request.method == "GET":
        editProject = editProjectFrom(instance=obj)
        return render(request, "projectManage/editProject.html", {"editProject": editProject})
    elif request.method == "POST":
        editProject = editProjectFrom(request.POST, instance=obj)
        if editProject.is_valid():
            editProject.save()
        else:
            executeInfo["status"] = "false"
            executeInfo["msg"] = editProject.errors
        return JsonResponse(executeInfo)

def delete_project(request, id):
    executeInfo = {"status": "true", "msg": None}
    if request.method == "GET":
        try:
            project.objects.get(id=id).delete()
        except Exception as err:
            executeInfo["status"] = "false"
            executeInfo["msg"] = "项目删除失败：%s", err
        return JsonResponse(executeInfo)

def index_delete_project(request,id):
    if request.method == "GET":
        project.objects.get(id=id).delete()
        return redirect("/BusinessInfo/project/index/")
