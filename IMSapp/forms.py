from django import forms
from .models import Building,Room,Exam,Invigilator,ExamSession

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
        fields="__all__"
        
class InvigilatorForm(forms.ModelForm):
    class Meta:
        model=Invigilator
        fields="__all__"
        
class ExamSessionForm(forms.ModelForm):
    class Meta:
        model=ExamSession
        fields="__all__"
    
class CsvUploadForm(forms.Form):
    csv_file = forms.FileField()