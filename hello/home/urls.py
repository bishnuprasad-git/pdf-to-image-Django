from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),
    path("services/", views.services, name='services'),
    path("contact/", views.contact, name='contact'),
    path("allprod/", views.prod_view, name='prod_view'),
    path("allprod/<str:s>", views.prod_view1, name='prod_view1'),
    path("checkout/", views.checkout, name='checkout'),
    path("tracker/", views.tracker, name='tracker')
]