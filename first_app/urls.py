from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('postsignup/',views.postsignup,name='postsignup'),
    path('logout/',views.logout,name='logout'),
    path('classes/',views.classes,name='classes'),
    path('timetable/',views.timetable,name='timetable'),
    path('students/',views.students,name='students'),
    path('attendance/',views.attendance,name='attendance'),
    path('editstudent/',views.editstudent,name='editstudent'),
    path('addstudents/',views.addstudents,name='addstudents'),
]