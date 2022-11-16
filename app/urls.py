from django.urls import path
from app.views import *



urlpatterns = [
    path('',index,name="index"),
    path('success',success,name="success"),
]
