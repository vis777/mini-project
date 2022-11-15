from django.conf.urls import url

from review import views

urlpatterns=[
    url('revi/',views.rev),
    url('prorev/',views.prodrev)

    ]