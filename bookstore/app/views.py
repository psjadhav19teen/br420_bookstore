from django.shortcuts import render
from .models import Books


# Create your views here.
def index(req):
    allbooks = Books.objects.all()
    print(allbooks)
    return render(req, "index.html")


def signup(req):
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
