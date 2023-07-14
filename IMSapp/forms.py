from django import forms
from .models import Building,Room,Exam

class BuildingForm(forms.ModelForm):
    class Meta:
        model=Building
        fields=("id","name")

class RoomForm(forms.ModelForm):
    class Meta:
        model=Room
        fields=("id","room_number","building")
        
class ExamForm(forms.ModelForm):
    class Meta:
        model=Exam
        fields=("name","semester","types","shift","start_time")
        
