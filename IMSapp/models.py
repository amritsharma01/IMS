from django.db import models

# Create your models here.
class Exam(models.Model):
    name=models.CharField(max_length=50)
    shift_choices=[
        ("morning","Morning"),
        ("day","Day")
    ]
    type_choices=[
        ("regular","Regular"),
        ("back","Back")
    ]
    semester_choices=[
        ("odd","Odd"),
        ("even","Even")
    ]
    semester= models.CharField(max_length=10,choices=semester_choices,default="Odd")
    types= models.CharField(max_length=10,choices=type_choices,default="Regular")
    shift= models.CharField(max_length=10,choices=shift_choices,default="Morning")
    
    def __str__(self):
        return f"{self.name} ({self.types},{self.semester},{self.shift})"
    
    
    
    
class Building(models.Model):
    name=models.CharField(max_length=50, unique=True)
        
    def __str__(self):
        return f"{self.name}"
        
class Room(models.Model):
    room_number=models.IntegerField()
    building=models.ForeignKey(Building, on_delete=models.CASCADE, default="ICTC")
    
    
    class Meta:
        unique_together=["building", "room_number"]
    
    def __str__(self):
        return f"Room.No {self.room_number} of {self.building.name}"
    
class Invigilator(models.Model):
    gender_choice=[
        ("male","Male"),
        ("female","Female"),
        ("other","Other")
    ]
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.CharField(max_length=50,unique=True)
    phone=models.CharField( max_length=50, unique=True)
    address=models.CharField( max_length=70,null=True)
    gender=models.CharField( max_length=50, choices=gender_choice,default="Male")
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    def is_invigilator_available(self, date, shift):
        return ExamSession.objects.filter(invigilators=self, shift=shift, date=date).exists()
    
class ExamSession(models.Model):
    shift_choices=[
        ("morning","Morning"),
        ("day","Day")
    ]
    
    
    shift= models.CharField(max_length=10,choices=shift_choices,default="Morning")
    date=models.DateField()
    room=models.ForeignKey(Room,  on_delete=models.CASCADE, default=1)
    invigilators=models.ForeignKey(Invigilator,on_delete=models.CASCADE,default=1)
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)

    def __str__(self):
        return f"Exam Session: {self.date}"
    
    class Meta:
        unique_together=["shift","date","invigilators"]
    
    