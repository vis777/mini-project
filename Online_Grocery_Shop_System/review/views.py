from django.shortcuts import render
from product.models import Product
from review.models import Review
import datetime
# Create your views here.
def rev(request):
    obj=Review.objects.all()
    context={
        'x':obj
    }
    return render(request,'review/viewreview.html',context)
    

def prodrev(request):
    obk=Product.objects.all()
    context={
        'kk':obk
    }
    if request.method=="POST":
        ob=Review()
        ob.userid="1"
        ob.review=request.POST.get('review')
        ob.date=datetime.datetime.today()
        ob.product_id=request.POST.get('pro')
        ob.rating=request.POST.get('rate')
        ob.save()
    return render(request,'review/product review.html',context)   