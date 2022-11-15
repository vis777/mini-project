from django.shortcuts import HttpResponseRedirect, render
from login.models import Login
# Create your views here.
def log(request):
    if request.method=="POST":
        name=request.POST.get('name')
        password=request.POST.get('psw')
        obj =Login.objects.filter(username=name,password=password)
        tp=""
        for ob in obj:
            tp=ob.type
            uid=ob.u_id
            if tp == "admin":
                request.session["uid"]=uid
                return HttpResponseRedirect('/temp/admin/')
            elif tp =="user":
                request.session['uid']=uid
                return HttpResponseRedirect('/temp/user/')
        else:
            obj1= "username or password incorrect.... please try"
            context={
                'msg':obj1,
            }
            return render(request,'login/login.html',context)
    return render(request,'login/login.html')