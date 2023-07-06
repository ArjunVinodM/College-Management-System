from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('Home_Page', views.home_page, name='Home_Page'),
    path('Signin_Page', views.signin_page, name='Signin_Page'),
    path('Signup_Page', views.signup_page, name='Signup_Page'),
    
    path('admin_home_page', views.admin_home_page, name='admin_home_page'),
    path('admin_add_course', views.admin_course, name='admin_add_course'),
    path('admin_add_student', views.admin_student, name='admin_add_student'),
    path('admin_show_student', views.show_stu, name='admin_show_student'),
    path('admin_show_teacher', views.show_tchr, name='admin_show_teacher'),
    
    path('teacher_registration', views.signup, name='teacher_registration'),
    path('login_user', views.userlogin, name='login_user'),
    
    path('course_adding', views.add_course, name='course_adding'),
    path('student_registration', views.add_student, name='student_registration'),
    
    path('user_home_page', views.user_home_page, name='user_home_page'),
    path('profile_view', views.view_profile , name='profile_view'),
    path('update_profile', views.updation, name='update_profile'),
    path('teacher_update/<int:pk>', views.update, name='teacher_update'),
    path('logout', views.logoutpage, name='logout'),
    
    path('delete_student/<int:pk>', views.delete_student, name='delete_student'),
    path('delete_teacher/<int:pk>', views.delete_teacher, name='delete_teacher'),
    
]
