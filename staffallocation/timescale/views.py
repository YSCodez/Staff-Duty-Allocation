import datetime
from http.client import HTTPResponse
from itertools import count
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout, get_user
from .models import ShiftDept, taskAllocA, Feedemp
from django.db.models import Count

# Create your views here.
def index(request):
    return render(request, 'timescale/index.html')

##.route("/index1")
def index1(request):
    return render(request,'timescale/index1.html')

#.route("/AdminSignIn")
def AdminSignIn(request):
    return render(request,'timescale/Adminsignin.html')

#.route("/AdminLogin")
def AdminLogin(request):
    taskList = taskAllocA.objects.all()
    return render(request, 'timescale/AdminLogin.html', {'taskList': taskList})

#.route("/Emppage")
def emppage(request):
    return render(request, 'timescale/employepage.html')

#.route("/Addemploy")
def Addemploy(request):
    return render(request,'timescale/Addemploy.html')

#.route("/taskallocation")
def  taskallocation(request):
    user = User.objects.all()
    print(user)
    return render(request, 'timescale/taskallocation.html', {'user': user})

#.route("/404Notfound")
def  Not(request):
    return render(request,'timescale/404.html')

#.route("/blank")
def  blank(request):
    return render(request, 'timescale/blank.html')

#.route("/Confirmation")
def  Conformation(request):
    return render(request, 'timescale/confirmationOnTask.html')

#.route("/assignedTaskem")
def  assignedTaskem(request):
    checkuser = get_user(request)
    taskList = taskAllocA.objects.all()
    return render(request,'timescale/assignedTask(em).html', {'checkuser':checkuser,'taskList': taskList})

#.route("/employeeComplainPage")
def  employeeComplainPage(request):
    return render(request,'timescale/employeeComplainPage.html')

def allocShift(request):
    getuser = User.objects.all()
    return render(request, 'timescale/allocShit.html', {'getuser':getuser})

#.route("/complainRegistered")
def  complainRegistered(request):
    return render(request,'timescale/complainRegistered.html')

#.route("/replyToComplain")
def  replyToComplain(request):
    return render(request,'timescale/replyToComplain.html')

#.route("/AssignTask")
def  AssignTask(request):
    return render(request,'timescale/AssignTask.html')

def addemploy(request):
    return render(request,'timescale/Addemploy.html')

def EmpHandle(request):
    return render(request,'timescale/employeehandle.html')

def Notfound(request):
    return render(request,'timescale/404.html')

#Database SignUp
def UserRegister(request):
    if request.method == 'POST':
        #Get the post parameters
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password= request.POST['password']
        confirmPassword= request.POST['confirmPassword']

        #Check for errorinput

        if password != confirmPassword:
            messages.error(request, "Passwords do not match!!")
            return redirect('/')

        if not username.isalnum():
            messages.error(request, "Username should contain only letters and numbers!!")
            return redirect('/')

        #Create User
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Timescale account was created successfully!!")
        return redirect('/index1/')

def UseradminRegister(request):
    if request.method == 'POST':
        #Get the post parameters
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password= request.POST['password']
        confirmPassword= request.POST['confirmPassword']

        #Check for errorinput

        if password != confirmPassword:
            messages.error(request, "Passwords do not match!!")
            return redirect('/')

        if not username.isalnum():
            messages.error(request, "Username should contain only letters and numbers!!")
            return redirect('/')

        #Create User
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Timescale account was created successfully!!")
        return redirect('/AdminLogin/')
        
    else:
        return HTTPResponse('404 - Not Found')

def handleLogin(request):
    if request.method == 'POST':
        #Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername, password = loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request, 'Successfully Logged In')
            return redirect('/Emppage/')
        else:
            messages.error(request, "Invalid Credentials, Please try again!!")
            return redirect('/index1/')
    return HTTPResponse('404-Not Found')

def handleAdminLogin(request):
    if request.method == 'POST':
        #Get the post parameters
        loginadminusername = request.POST['floatingInput']
        loginadminpassword = request.POST['floatingPassword']

        adminuser = authenticate(username = loginadminusername, password = loginadminpassword )

        if adminuser is not None:
            login(request,adminuser)
            messages.success(request, 'Successfully Logged In')
            return redirect('/AdminLogin/')
        else:
            messages.error(request, "Invalid Credentials, Please try again!!")
            return redirect('/AdminSignIn/')
    return HTTPResponse('404-Not Found')

def handleadminLogout(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out!!')
    return redirect("/")

def handleuserLogout(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out!!')
    return redirect("/")

def getTask(request):
    if request.method == 'POST':
        #Get the post parameters
        user = request.POST.get('User')
        date = request.POST['duedate']
        time = request.POST['duetime']
        username = request.POST['username']
        task = request.POST['taskalloc']
        
        ins = taskAllocA(user = user,date = date, time = time,username = username, task = task)
        ins.save()
        return redirect('/Confirmation/')
    return HTTPResponse('404-Not Found')

def getFeed(request):
    if request.method == 'POST':
        #Get the post parameters
        fname = request.POST['fname']
        email = request.POST['email']
        feed = request.POST['feed']
        date_time = datetime.datetime.now()

        ins = Feedemp(fname = fname, email = email, date_time = date_time, feed = feed)
        ins.save()
        return redirect('/complainRegistered/')
    else:
        return HTTPResponse('404-Not Found')

def adminfeed(request):
    eventList = Feedemp.objects.all()
    return render(request, 'timescale/employeehandle.html', {'eventList': eventList})

def delete_Feed(request, event_id):
    event = Feedemp.objects.filter(pk=event_id)
    event.delete()
    messages.success(request, 'Successfully Deleted!!')
    return redirect('/data/')

def emptaskdelete(request, event_id):
    event = taskAllocA.objects.filter(pk=event_id)
    event.delete()
    messages.success(request, 'Successfully Deleted!!')
    return redirect('/AdminLogin/')

def delete(request):
    event = taskAllocA.objects.all()
    event.delete()
    messages.success(request, 'Successfully Deleted!!')
    return redirect('/')

def allocShit(request):
    if request.method == 'POST':
        #Get the post parameters
        shift = request.POST['ShiftSelect']
        dept = request.POST['Department']

        ins = ShiftDept(shift=shift, dept = dept)
        ins.save()
        return redirect('/AdminLogin/')
    else:
        return HTTPResponse('404-Not Found')