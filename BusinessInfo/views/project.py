"""
    项目管理-视图
"""
from django.shortcuts import render, redirect
from BusinessInfo.models import project
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from BusinessInfo.forms.addProject import addProjectFrom
from django.http import JsonResponse
from django.contrib.auth.models import User


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


def detail_project(request, id):
    obj = project.objects.filter(id=id).first()
    if request.method == "GET":
        return render(request, "details/detail.html", {"editProject": obj})


# 项目标星
def star_project(request):
    executeInfo = {"status": "true", "msg": None}
    if request.method == "GET":
        productID = request.GET["id"]
        username = User.objects.get(username=request.user)
        project.objects.get(id=productID).star.add(username)
        return JsonResponse(executeInfo)

# 取消标星
def cancelStar_project(request):
    executeInfo = {"status": "true", "msg": None}
    if request.method == "GET":
        productID = request.GET["id"]
        username = User.objects.get(username=request.user)
        project.objects.get(id=productID).star.remove(username)
        return JsonResponse(executeInfo)
