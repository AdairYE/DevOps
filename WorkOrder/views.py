from django.shortcuts import render


# Create your views here.
def toBase(request):
    if request.method == "GET":
        return render(request, "workorder/base.html", {"name": 1})
