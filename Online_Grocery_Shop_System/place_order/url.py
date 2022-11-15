from django.conf.urls import url

from place_order import views

urlpatterns=[
    url('plcord/',views.placeord),
    url('vord/',views.vieword),
    url('cart/(?P<idd>\w+)',views.addcart),
    url('dtl/(?P<idd>\w+)',views.remove),
    url('update/(?P<idd>\w+)',views.updateqt),
    url('vieworder/',views.viewor)
    ]