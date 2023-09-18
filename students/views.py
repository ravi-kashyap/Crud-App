from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import student 

# Create your views here.

def home(request):
    std = student.objects.all()

    return render(request, "students/home.html", {"std": std})

def add_student(request):
    if request.method == "POST": 
        Name = request.POST.get("std_name")
        Password = request.POST.get("std_password")
        Email = request.POST.get("std_email")
        Phone = request.POST.get("std_phone")
        Roll = request.POST.get("std_roll")
        Address = request.POST.get("std_address")

        #create an object for model 
        s=student() 
        s.name = Name
        s.password = Password
        s.email = Email
        s.phone = Phone 
        s.roll = Roll 
        s.address = Address
        s.save()
        return redirect("/students/home")

    return render(request, "students/add_student.html",{})


def del_student(request):

    return render(request, "students/del_student.html",{})


def remove_student(request, roll):
    s = student.objects.get(pk= roll)
    s.delete()

    return redirect("/students/home")


def edit_student(request,roll):
    s = student.objects.get(pk = roll)

    return render(request, "students/edit_student.html", {"s":s})

def update_student(request, roll):
    Name = request.POST.get("std_name")
    Password = request.POST.get("std_password")
    Email = request.POST.get("std_email")
    Phone = request.POST.get("std_phone")
    Roll = request.POST.get("std_roll")
    Address = request.POST.get("std_address")
 
    #create an object for model 
    s=student() 
    s.name = Name
    s.password = Password
    s.email = Email
    s.phone = Phone 
    s.roll = Roll 
    s.address = Address
    s.save()
    return redirect("/students/home")
    
