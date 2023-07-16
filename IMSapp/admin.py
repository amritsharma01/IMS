from django.contrib import admin
from .models import Exam,Building,Room,Invigilator,ExamSession
# Register your models here.

admin.site.register(Building)
admin.site.register(Room)
admin.site.register(Invigilator)

@admin.register(ExamSession)
class ExamSessionAdmin(admin.ModelAdmin):
    list_display = ("id", "invigilators", "date", "shift", "room")
    
    def save_model(self, request, obj, form, change):
        # if form.is_valid():
        #     invigilator = form["invigilators"]
        #     shift = form["shift"]
        #     date = form["date"]
        #     if not invigilator.is_invigilator_available(shift, date):
        #         raise form.ValidationError({"invigilator": "This is used"})
        #     print(form)
        super().save_model(request, obj, form, change)

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "shift", "semester","types")
    
    def save_model(self, request, obj, form, change):
       
        super().save_model(request, obj, form, change)