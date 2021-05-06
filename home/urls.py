from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.index,name='home'),
    path("about", views.about,name='about'),      # here the name is function name in views.py
    path("services", views.services,name='services'),
    path("contact", views.contact,name='contact'),
]