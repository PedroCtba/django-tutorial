from nturl2path import url2pathname
import django
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]