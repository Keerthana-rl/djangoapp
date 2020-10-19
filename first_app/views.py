from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
import pyrebase
from django.contrib.auth import logout
# Create your views here.
config = {
    'apiKey': "AIzaSyDM8YdHApmPrmqomMK485TPxI9F4IPQ-vg",
    'authDomain': "webapp-63e8f.firebaseapp.com",
    'databaseURL': "https://webapp-63e8f.firebaseio.com",
    'projectId': "webapp-63e8f",
    'storageBucket': "webapp-63e8f.appspot.com",
    'messagingSenderId': "368042170003",
    'appId': "1:368042170003:web:fcb8be3e07223ab90edf66"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return render(request,'index.html') 
    
def classes(request):
    Teacher_ID=request.POST.get('Teacher_ID')
    email=request.POST.get('email')
    password=request.POST.get('password')
    try:
        user = authe.sign_in_with_email_and_password(email,password)
    except:
        message="invalid credentials"
        return render(request,'index.html',{"messg":message})
    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    

    return render(request,'classes.html',{"e":Teacher_ID})
    

def timetable(request):
    return render(request,'timetable.html')
def students(request):
    return render(request,'students.html')
def editstudent(request):
    return render(request,'editstudent.html')
def attendance(request):
    return render(request,'attendance.html')

def addstudents(request):
    return render(request,'addstudents.html')

def postsignup(request):
    Teacher_ID=request.POST.get('Teacher_ID')
    email=request.POST.get('email')
    password=request.POST.get('password')
    
    user=authe.create_user_with_email_and_password(email,password)
    
    uid = user['localId']
    data ={"Teacher_id":Teacher_ID,"status":"1"}

    database.child("staffs").child(uid).child("details").set(data)
    return render(request,'index.html')
