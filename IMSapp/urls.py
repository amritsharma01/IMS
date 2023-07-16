from . import views
from django.urls import path
app_name="IMSapp"
urlpatterns = [
    path("",views.index,name="index"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("buildings/",views.buildings,name="buildings"),
    path("rooms/",views.rooms,name="rooms"),
    path("exams/",views.exams,name="exams"),
    path("invigilators/",views.invigilators,name="invigilators"),
    path("examsessions/",views.examsessions,name="examsessions")
    
]
