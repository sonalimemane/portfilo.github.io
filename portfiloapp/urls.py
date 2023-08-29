from django.contrib import admin
from django.urls import path
from portfiloapp import views



urlpatterns = [
    path('', views.home, name='home'),
    path('project', views.project, name='project'),
    path('contact', views.contact, name='contact'),
    ]