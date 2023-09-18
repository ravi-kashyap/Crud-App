from django.contrib import admin
from django.urls import path
from . import views 
# from .views import *

urlpatterns = [
    path('',views.home, name="home"),
    path('home',views.home, name= "home"),
    path('add_student',views.add_student,name="add_student"),
    path('del_student',views.del_student,name="del_student"),
    path('remove_student/<int:roll>',views.remove_student, name="remove_student"),
    path('edit_student/<int:roll>',views.edit_student, name="edit_student"),
    path('update_student/<int:roll>',views.update_student, name= "update_student"),
    ]