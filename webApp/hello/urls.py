from django.urls import path

# here . means the current directory
from . import views

#here the url routes are defined
urlpatterns=[
    path("",views.home, name="home"),

    #greet function
    path("<str:name>",views.greet,name="greet"),
    path("manish",views.Manish, name="Manish"),
    path("ujjwal",views.Ujjwal,name="ujjwal")
]