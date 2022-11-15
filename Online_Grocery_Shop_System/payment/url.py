from django.conf.urls import url

from payment import views

urlpatterns=[
    url('paym/',views.pay),
    url('viewp/',views.viewpay)
    ]