from django.contrib import admin
from .models import Exam,Building,Room,Invigilator,ExamSession
# Register your models here.
admin.site.register(Exam)
admin.site.register(Building)
admin.site.register(Room)
admin.site.register(Invigilator)
admin.site.register(ExamSession)