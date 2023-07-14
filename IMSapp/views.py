from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import BuildingForm,RoomForm,ExamForm
from IMSapp.models import Building,Room,Exam

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
    
    if request.method=="POST":
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        username= request.POST["username"]
        pass1=request.POST["password1"]
        pass2=request.POST["password2"]
        if(pass1!=pass2):
             return render(request,"register.html",{
                "message":"passwords donot match"
            })
        checkexist=User.objects.filter(username=username)
        if checkexist.exists():
            return render(request,"register.html",{
                "message":"User already exists"
            })
        else:
            user=User.objects.create(first_name=firstname,last_name=lastname,username=username)
            user.set_password(request.POST["password1"])
            user.save()
            return render(request,"login.html",{
                "message":"User Created Succesfully!"
            })
            
       
    
    return render(request,"register.html")

@login_required(login_url="IMSapp:login")
def buildings(request):
    buildinglist=Building.objects.all()
    if request.method=="POST":
        print("hai")
        form=BuildingForm(request.POST)
        if form.is_valid():
            print("hi")
            form.save()
        else:
            print(form.errors.as_data())
            
        
    return render(request,"building.html",{
        
        "buildings":buildinglist
    })
        
@login_required(login_url="IMSapp:login")
def rooms(request):
    roomslist=Room.objects.all()
    buildinglist=Building.objects.all()
    if request.method=="POST":
        form=RoomForm(request.POST)
        if form.is_valid():
            print("hi")
            form.save()
        else:
            print(form.errors.as_data())
            
        
    return render(request,"rooms.html",{
        
        "rooms":roomslist,
        "buildings":buildinglist
    })
        
@login_required(login_url="IMSapp:login")
def exams(request):
    examlist=Exam.objects.all()
    if request.method=="POST":
        form=ExamForm(request.POST)
        if form.is_valid():
            print("hi")
            form.save()
        else:
            print(form.errors.as_data())
            
        
    return render(request,"exams.html",{
        
        "exams":examlist,
    })