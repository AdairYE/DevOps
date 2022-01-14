from django.shortcuts import render,redirect

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        print("asd",username)
        print("asd",password)
    return render(request,'login/login.html')
