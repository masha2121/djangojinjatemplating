from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='My_home'),
    path('contact/', views.contact, name='My_contact'),
    path('about/', views.about, name='My_about'),
    path('gallery',views.gallery,name='My_gallery')

]