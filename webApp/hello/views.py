from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

#here we create the home function to return the  httpResponse
#based on the http requests

#when you  want tpo render the files like html,
#use render function and pass in request object and file path
def home(request):
    return render(request,"hello/index.html")

#instead of the greeting individually , ets create a greet fn
def greet(request,name):
    return render(request,"hello/greet.html",{
        "name":name.capitalize()
    })
    # return HttpResponse(f"Hello {name.capitalize()}!")
#my own function
def Manish(request):
    return HttpResponse("HEllo Manish")

def Ujjwal(request):
    return HttpResponse("Hello Ujjwal")