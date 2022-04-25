"""
    项目管理-视图
"""
from django.shortcuts import render, redirect
from BusinessInfo.models import project
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from BusinessInfo.froms.addProject import addProjectFrom
from BusinessInfo.froms.editProject import editProjectFrom
from django.http import JsonResponse


def projectIndex(request):
    executeInfo = {"status": "true", "msg": None}
    if request.method == "GET":
        projectMeta = project._meta.fields
        addproject = addProjectFrom()

        user_StarProject = project.objects.filter(star=request.user)
        user_CreateProject = project.objects.filter(author=request.user).exclude(id__in=user_StarProject)
        user_PartProject = project.objects.filter(participator=request.user).exclude(id__in=user_StarProject)

        return render(
            request,
            "projectManage/index.html",
            {
                "proNameList": projectMeta,
                "addproject": addproject,
                "user_CreateProject": user_CreateProject,
                "user_StarProject": user_StarProject,
                "user_PartProject": user_PartProject
            }
        )
    elif request.method == "POST":
        addproject = addProjectFrom(request.POST)
        if addproject.is_valid():
            proName = addproject.save()
            update_author = project.objects.get(name=proName)
            update_author.author = request.user
            update_author.save()
        else:
            executeInfo["status"] = "false"
            executeInfo["msg"] = addproject.errors
        return JsonResponse(executeInfo)


def edit_project(request, id):
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


def index_delete_project(request, id):
    if request.method == "GET":
        project.objects.get(id=id).delete()
        return redirect("/BusinessInfo/project/index/")
