from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("IMSapp:login"))
    return render(request,"home.html",{
        "variable": request.user
    }
        
    )
                  

def login_view(request):
    if request.method=="POST":
        username= request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password )
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("IMSapp:index"))
        else:
            return render(request, "login.html",{
                "message": "Not the vaild credentials"
            })
    
    return render(request,"login.html")

def logout_view(request):
    logout(request)
    return render(request,"login.html",{
        "message":"Logged Out"
    })
    

def register(request):
    return render(request,"register.html",{
       
    })