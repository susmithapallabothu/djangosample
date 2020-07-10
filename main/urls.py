from django.contrib import admin
from django.urls import path
from  main import views
urlpatterns = [
    path('',views.index,name="home"),
    path('main/sign_up/',views.sign_up,name="sign_up")
]