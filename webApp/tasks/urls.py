from django.urls import path
from . import views
urlpatterns=[
    path("",views.hometask,name="hometask"),
    path("add",views.add,name="add")
]