from django.conf.urls import url

from product import views

urlpatterns=[
    # url('prodr/',views.prodrev),
    url('produc/',views.product),
    url('vprod/',views.viewprod),
    url('buy/(?P<idd>\w+)',views.pr_buy)
    ]