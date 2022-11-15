from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('hello')
    return render(request,'temp/index.html')

def admin(request):
    # return HttpResponse('hello')
    return render(request,'temp/admin.html')

def user(request):
    # return HttpResponse('hello')
    return render(request,'temp/user.html')

