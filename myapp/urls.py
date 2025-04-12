from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('services/', views.services, name='services'),
    path('contactme/', views.contactme, name='contactme'),
]
