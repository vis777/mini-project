from django.conf.urls import url

from temp import views

urlpatterns=[
    url('index/',views.home),
    url('admin/',views.admin),
    url('user/',views.user)
    ]
