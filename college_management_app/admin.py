from django.contrib import admin
from college_management_app.models import CourseModel,TeacherModel,StudentModel

# Register your models here.
@admin.register(CourseModel)
class CourseDetailAdmin(admin.ModelAdmin):
  list_display = ('id', 'Course_Name', 'Course_Fee')
  
@admin.register(TeacherModel)
class TeacherDetailAdmin(admin.ModelAdmin):
  list_display = ('id', 'Course', 'Tchr_Age', 'Tchr_Address', 'Tchr_Gender', 'Tchr_Phone', 'Tchr_Image', 'Tchr_Joining_Date')
  
@admin.register(StudentModel)
class StudentDetailAdmin(admin.ModelAdmin):
  list_display = ('id', 'Course', 'Stu_first_name', 'Stu_last_name', 'Stu_age', 'Stu_address', 'Stu_gender', 'Stu_phone', 'Stu_email', 'Stu_image', 'Stu_joining_date')