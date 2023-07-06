from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CourseModel(models.Model):
  Course_Name = models.CharField(max_length=50)
  Course_Fee = models.IntegerField() 
  
class TeacherModel(models.Model):
  Course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, null=True)
  Teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  Tchr_Age = models.IntegerField()
  Tchr_Address = models.CharField(max_length=255)
  Tchr_Gender = models.CharField(max_length=10)
  Tchr_Phone = models.IntegerField()
  Tchr_Image = models.ImageField(upload_to='image/', null=True)
  Tchr_Joining_Date = models.DateField(auto_now_add=True)
  
class StudentModel(models.Model):
  Course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, null=True)
  Stu_first_name = models.CharField(max_length=255)
  Stu_last_name = models.CharField(max_length=255)
  Stu_age = models.IntegerField()
  Stu_address = models.CharField(max_length=255)
  Stu_gender = models.CharField(max_length=10)
  Stu_phone = models.IntegerField()
  Stu_email = models.CharField(max_length=50)
  Stu_image = models.ImageField(upload_to='image/', null=True)
  Stu_joining_date = models.DateField(auto_now_add=True)
  
  
  
