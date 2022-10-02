from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('regis',views.registration),
    path('main',views.home1)
]