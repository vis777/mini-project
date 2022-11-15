from multiprocessing import context
from django.shortcuts import render
import datetime 
# Create your views here.
from complaint.models import Complaint
def com(request):
    ss=request.session["uid"]
    if request.method=="POST":
        ob=Complaint()
        ob.complaint=request.POST.get('comp')
        ob.user_id=ss
        ob.date=request.POST.get('date')
        ob.reply="pending"
        ob.save()
    return render(request,'complaint/complaint.html')
def repl(request,idd):
    if request.method=="POST":
        obb=Complaint.objects.get(com_id=idd)
        obb.reply=request.POST.get('repl')
        obb.save()
    return render(request,'complaint/reply.html')
def viewcom(request):
    obj=Complaint.objects.all()
    context={
        'y':obj
    }
    return render(request,'complaint/viewcomplaint.html',context) 
def viewrepl(request):
    obj=Complaint.objects.all()
    context={
        't':obj
    }
    return render(request,'complaint/vreply.html',context)          
