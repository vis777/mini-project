from django.conf.urls import url

from complaint import views

urlpatterns=[
    url('comp/',views.com),
    url('rep/(?P<idd>\w+)',views.repl),
    url('view/',views.viewcom),
    url('vrepl/',views.viewrepl)
]