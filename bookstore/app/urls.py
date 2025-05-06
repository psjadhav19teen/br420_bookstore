from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    # path("", views.DTLdemo),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('userlogout/',views.userlogout,name='userlogout')
]
