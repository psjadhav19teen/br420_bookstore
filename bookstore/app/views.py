from django.shortcuts import render,redirect
from .models import Books


# Create your views here.
def index(req):
    allbooks = Books.objects.all()
    print(allbooks)
    # b=Books.objects.create(bookid=117,title='mongodb',author='mm',category='Database',price=1000,qty=3,dop='2000-02-21',photo=None)
    # b.save()

    # b=Books.objects.get(bookid=117)
    # b.author='mayur k'
    # b.save()

    # b=Books.objects.filter(bookid=117).first()
    # b.author='manojkumar'
    # b.save()
    context={'allbooks':allbooks}
    return render(req, "index.html",context)


from django.contrib import messages
from django.contrib.auth.models import User

def signup(req):
    print(req.method) #navbar <a>
    if req.method=="POST":
        print(req.method) #POST
        uname=req.POST.get('uname')
        uemail=req.POST.get('uemail')
        upass=req.POST.get('upass')
        ucpass=req.POST.get('ucpass')
        print(uname,uemail,upass,ucpass)
        user=User.objects.values_list('username',flat=True)
        print(user)
        chkemail=User.objects.values_list('email',flat=True)
        print(chkemail)

        if upass!=ucpass:
            # errmsg="Password and confirm password doesn't match. Try again"
            # context={'errmsg':errmsg}
            # return render(req,'signup.html',context)

            messages.error(req,"Password and confirm password doesn't match. Try again")
            return render(req,'signup.html')
        elif uname==upass:
            messages.error(req,"Username and password must be different.")
            return render(req,'signup.html')
        elif uname in user:
            messages.error(req,"Username already exists.Try again")
            return render(req,'signup.html')
        elif uemail in chkemail:
            messages.error(req,"Email already exists.Try again")
            return render(req,'signup.html')
            
        newuser=User.objects.create(username=uname,email=uemail,password=upass)
        newuser.set_password(upass)
        newuser.save()
        print(User.objects.all())
        
        messages.success(req,"Registration done successfully!")
        return render(req, "signin.html")
    else:
        print(req.method) #GET (when refresh)
        return render(req, "signup.html")


from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import check_password

def signin(req):
    if req.method=="POST":
        # uname=req.POST.get("uname")
        uemail=req.POST.get("uemail")
        upass=req.POST.get("upass")
        print(uemail,upass)
        # userdata=User.objects.filter(email=uemail,password=upass) #not work
        # userdata=authenticate(username=uname,password=upass)
        # print(userdata) #check user
        try:
            chkemail=User.objects.get(email=uemail)
            print(chkemail)
            if  chkemail.check_password(upass):
                login(req,chkemail)
                return render(req,'dashboard.html')
            else:
                messages.error(req,'Incorrect password')
                return render(req,'signin.html')
        except User.DoesNotExist:
            messages.error(req,'Emailid Not exists')
            return render(req,'signin.html')

    
    else:
        return render(req, "signin.html")


def dashboard(req):
    return render(req, "dashboard.html")


def userlogout(req):
    logout(req)
    return redirect("/")


def about(req):
    return render(req, "about.html")


def contact(req):
    return render(req, "contact.html")


from datetime import datetime


def DTLdemo(req):
    # name="vedant"
    # return render(req, "DTLdemo.html",{'name':name})

    name = "vedant"
    curdatetime = datetime.now()
    greeting = "Good evening"
    curhour = datetime.now().hour
    print(curhour)
    password = "admin"
    authors = ["pp", "jj", "cc"]
    students = {
        101: {"name": "pooja", "issuedbook": "python"},
        102: {"name": "raj", "issuedbook": "java"},
    }
    context = {
        "name": name,
        "curdatetime": curdatetime,
        "greeting": greeting,
        "password": password,
        "curhour": curhour,
        "authors": authors,
        "students": students,
    }

    return render(req, "DTLdemo.html", context)
