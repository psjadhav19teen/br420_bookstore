from django.shortcuts import render
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
            messages.error(req,"Username and password be different.")
            return render(req,'signup.html')
        elif uname in user:
            messages.error(req,"Username already exists.Try again")
            return render(req,'signup.html')
        elif uemail in chkemail:
            messages.error(req,"Email already exists.Try again")
            return render(req,'signup.html')
            
        newuser=User.objects.create(username=uname,email=uemail,password=upass)
        newuser.set_password()
        newuser.save()
        print(User.objects.all())
        
        messages.success(req,"Registration done successfully!")
        return render(req, "signin.html")
    else:
        print(req.method) #GET (when refresh)
        return render(req, "signup.html")


def signin(req):
    return render(req, "signin.html")


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
