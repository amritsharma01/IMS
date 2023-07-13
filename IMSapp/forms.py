from django import forms
from .models import Building,Room

class BuildingForm(forms.ModelForm):
    class Meta:
        model=Building
        fields=("id","name")

class RoomForm(forms.ModelForm):
    class Meta:
        model=Room
        fields=("id","room_number","building")