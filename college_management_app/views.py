from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import *

# Create your views here.
def home_page(request):
  return render(request, 'home.html')

def signin_page(request):
  return render(request, 'signin.html')

def signup_page(request):
  course = CourseModel.objects.all()
  return render(request, 'signup.html', {'course':course})



def signup(request):
  if request.method == 'POST':
    fname = request.POST['t_first_name']
    lname = request.POST['t_last_name']
    age = request.POST['t_age']
    address = request.POST['t_address']
    gender = request.POST['t_gender']
    phone = request.POST['t_phn_no']
    
    select = request.POST['t_select_course']
    course = CourseModel.objects.get(id = select)
    
    uname = request.POST['t_user_name']
    email = request.POST['t_email']
    password = request.POST['t_password']
    con_password = request.POST['t_cpassword']
    
    image = request.FILES.get('t_file')
    
    if password == con_password:
      if User.objects.filter(username = uname).exists():
        messages.info(request, 'Username already exists...!')
        return redirect('Signup_Page')
      elif User.objects.filter(email = email).exists():
        messages.info(request, 'Email already exists...!')
        return redirect('Signup_Page')
      else:
        user = User.objects.create_user(first_name = fname,
                                        last_name = lname,
                                        email = email,
                                        username = uname,
                                        password = password)
        user.save()
        
        data = User.objects.get(id = user.id)
        Tchr_data = TeacherModel(Tchr_Age = age,
                            Tchr_Address = address,
                            Tchr_Gender = gender,
                            Tchr_Phone = phone,
                            Tchr_Image = image,
                            Course = course,
                            Teacher = data)
        Tchr_data.save()
        messages.success(request, 'Welcome'+ '' + data.first_name +' '+data.last_name + '' +'Please Login')
        return redirect('Signin_Page')
    else:
      messages.info(request, 'Your Password Does Not Match....!')
      return redirect('Signup_Page')
  else:
    return redirect('Signup_Page')
  


def userlogin(request):
  if request.method == 'POST':
    uname = request.POST['Username']
    passw = request.POST['Password']
    user = auth.authenticate(username = uname, password = passw)
    if user is not None:
      if user.is_staff:
        login(request, user)
        return redirect('admin_home_page')
      else:
        auth.login(request, user)
        return redirect('user_home_page')
    else:
      messages.info(request, 'No User Match Found Please SignUp....!')
      return redirect('Signup_Page')
  else:
    return redirect('Signin_Page')
  
  
  



def admin_home_page(request):
  return render(request, 'admin_home_page.html')

def admin_course(request):
  return render(request, 'add_course.html')

def admin_student(request):
  course = CourseModel.objects.all()
  return render(request, 'add_student.html', {'course': course})




def add_course(request):
  if request.method == 'POST':
    cname = request.POST['cou_name']
    cfee = request.POST['cou_fee']
    add_cou = CourseModel(Course_Name = cname,
                          Course_Fee = cfee)
    add_cou.save()
    print('hi')
    return redirect('admin_add_course')
  
def add_student(request):
  if request.method == 'POST':
    fir_name = request.POST['s_first_name']
    las_name = request.POST['s_last_name']
    age = request.POST['s_age']
    address = request.POST['s_address']
    gender = request.POST['s_gender']
    phone = request.POST['s_phn_no']
    
    select = request.POST['s_select_course']
    course = CourseModel.objects.get(id = select)
    
    email = request.POST['s_email']
    image = request.FILES.get('s_file')
    add_stu = StudentModel(Stu_first_name = fir_name,
                           Stu_last_name = las_name,
                           Stu_age = age,
                           Stu_address = address,
                           Stu_gender = gender,
                           Stu_phone = phone,
                           Stu_email = email,
                           Stu_image = image,
                           Course = course)
    add_stu.save()
    print('hi')
    return redirect('admin_show_student')
  
  
def show_stu(request):
  student = StudentModel.objects.all()
  context = {'students': student}
  return render(request, 'show_students.html', context)

def show_tchr(request):
  teacher = TeacherModel.objects.all()
  return render(request, 'show_teachers.html', {'teachers' : teacher})





def user_home_page(request):
  return render(request, 'user_home_page.html')

@login_required
def view_profile(request):
  teacher_view = TeacherModel.objects.get(Teacher = request.user)
  return render(request, 'show_teacher_profile.html', {'tchr':teacher_view})

def updation(request):
  Teacher = TeacherModel.objects.get(Teacher = request.user)
  return render(request, 'update_teacher_profile.html', {'tchr':Teacher})

@login_required
def update(request, pk):
  if request.method == 'POST':
    update = TeacherModel.objects.get(id = pk)
    f_name = request.POST['u_first_name']
    l_name = request.POST['u_last_name']
    email = request.POST['u_email']
    update.Tchr_Age = request.POST.get('u_age')
    update.Tchr_Address = request.POST.get('u_address')
    update.Tchr_Gender = request.POST.get('u_gender')
    update.Tchr_Phone = request.POST.get('u_phn_no')
    old = update.Tchr_Image
    new = request.FILES.get('u_file')
    if old != None and new == None:
      update.Tchr_Image = old
    else:
      update.Tchr_Image = new
      
    update.save()
    
    user = request.user
    user.first_name = f_name
    user.last_name = l_name
    user.email = email
    
    user.save()
    
    return redirect('profile_view')
  
def logoutpage(request):
    auth.logout(request)
    return redirect('Home_Page')
  
#  another way for logout
#def log(request):
#    request.session.flush()
#    auth.logout(request)
#    return redirect('Home_Page')

def delete_student(request, pk):
  student = StudentModel.objects.get(id = pk)
  student.delete()
  return redirect('admin_show_student')

def delete_teacher(request, pk):
  teacher = TeacherModel.objects.get(id = pk)
  teacher.delete()
  return redirect('admin_show_teacher')