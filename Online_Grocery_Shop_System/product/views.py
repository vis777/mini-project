from django.shortcuts import HttpResponseRedirect, render
from product.models import Product
from place_order.models import Order
from django.core.files.storage import FileSystemStorage
# Create your views here.
# def prodrev(request):
#     if request.method=="POST":
#         ob=Product()
#         ob.review=request.POST.get('review')
#         ob.date=request.POST.get('date')
#         ob.time=request.POST.get('time')
#         ob.save()
#     return render(request,'product/product review.html')

def product(request):
    if request.method=="POST":
        ob=Product()
        ob.productname=request.POST.get('pname')
        ob.description=request.POST.get('dname')
        ob.price=request.POST.get('price')
        ob.stock=request.POST.get('stock')
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        ob.image=myfile.name
        ob.shopid="1"
        ob.save()
    return render(request,'product/product.html')
def viewprod(request):
    if request.method=="POST":
        vv=request.POST.get('search')
        obj=Product.objects.filter(productname__istartswith=vv)
        context={
            'ok':obj
        }
    else:
        obj=Product.objects.all()
        context={
            'ok':obj
        }    
    return render(request,'product/viewprod.html',context)   


def pr_buy(request,idd):
    ob=Product.objects.get(prod_id=idd)
    obj=Order()
    # obj.order_id=idd
    obj.quantity=1
    obj.amount=ob.price
    obj.prod_id=idd
    obj.status="ok"
    obj.save()
    ob.stock=int(ob.stock)-obj.quantity
    ob.save()
    return HttpResponseRedirect('/place_order/vord/')
