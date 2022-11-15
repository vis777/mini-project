import http
from http.client import HTTPResponse
from re import I
from django.shortcuts import render
from place_order.models import Order
from place_order.models import Cart
from product.models import Product
from django.http import HttpResponseRedirect
# Create your views here.
def placeord(request):
    if request.method=="POST":
        ob=Order()
        ob.amount=request.POST.get('amount')
        ob.quantity=request.POST.get('quantity')
        ob.status=request.POST.get('status')
        ob.save()
    return render(request,'place_order/place order.html')

def vieword(request):
    obj=Order.objects.all()
    context={
        'ok':obj
    }
    return render(request,'place_order/vieworder.html',context)    

def updateqt(request,idd):
    if request.method=='POST':
        obj=Order.objects.get(order_id=idd)
        obj.quantity=request.POST.get('quantity')
        a=obj.prod_id
        b=obj.quantity
        obj.save()
        ob=Product.objects.get(prod_id=a)
        c=float(ob.stock)-float(b)
        ob.stock=float(c)+1
        ob.save()
        return vieword(request)
    return render(request,'place_order/update_qua.html')

def addcart(request,idd):
    obj=Order.objects.get(order_id=idd)
    ob=Cart()
    ob.order_id=idd
    ob.price=obj.amount
    ob.quantity=obj.quantity
    ob.save()
    return HttpResponseRedirect("/payment/paym/")
    # return render(request,'place_order/vieworder.html')   
    # 
    # 
    # 
def remove(request,idd):
    obj=Order.objects.get(order_id=idd)
    a=obj.quantity
    b=obj.prod_id
    ob=Product.objects.get(prod_id=b)
    ob.stock=float(ob.stock)+float(a)
    ob.save()
    obj.delete()
    
    return vieword(request)


def viewor(request):
    obj=Order.objects.all()
    context={
        'ok':obj
    }
    return render(request,'place_order/vieword.html',context) 