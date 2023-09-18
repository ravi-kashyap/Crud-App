# Created by Me - Ravi
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello ravi")

def home(request):
    num1 = 12
    num2 = 12
    return HttpResponse(num1 + num2)

def student(request):
    return HttpResponse("this is view for student")
