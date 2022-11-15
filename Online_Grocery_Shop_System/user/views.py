from django.shortcuts import render
from user.models import Registeration
from login.models import Login

# Create your views here.
def userreg(request):
     if request.method=="POST":
        ob=Registeration()
        ob.first_name=request.POST.get('fname')
        ob.last_name=request.POST.get('lname')
        ob.username=request.POST.get('name')
        ob.password=request.POST.get('psw')
        ob.gender=request.POST.get('gender')
        ob.email_id=request.POST.get('mail')
        ob.place=request.POST.get('place')
        ob.post=request.POST.get('post')
        ob.pin=request.POST.get('pin')
        ob.phone=request.POST.get('phone')
        ob.save()
        obb=Login()
        obb.username=ob.username
        obb.password=ob.password
        obb.u_id=ob.reg_id
        obb.type="user"
        obb.save()
     return render(request,'user/registration.html')
   