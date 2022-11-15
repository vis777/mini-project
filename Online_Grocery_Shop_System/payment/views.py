from django.shortcuts import render
from place_order.models import Order
from payment.models import Payment
from django.shortcuts import HttpResponseRedirect
# from product.models import Product
# Create your views here.
def pay(request):
   
    obj=Order.objects.all()
    a=0
    for i in obj:
        total=i.quantity*i.amount
        a=a+total
        context={
            'a':a
        }
    

    if request.method=="POST":
        ob=Payment()
        ob.card_holdername=request.POST.get('name')
        ob.cvv=request.POST.get('cvv')
        ob.card_number=request.POST.get('cardnumber')
        ob.amount=request.POST.get('amount')
        ob.save()
        objlist="payment successfull"
        context={
            'msg':objlist
            
        }
        # return HttpResponseRedirect('/product/vprod/')

    return render(request,'payment/payment.html',context)
    
def viewpay(request):
    obj=Payment.objects.all()
    context={
        't':obj
    }
    return render(request,'payment/pay.html',context)

