from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def about(request):
    #return HttpResponse("Hello World Example of PFSD Program")
     return render(request,'about.html')

def newuserregister(request):
  if request.method=='POST':

    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")
    firstname=request.POST.get("firstname")


  return render(request,'newuserregister.html')



def contact(request):
    return render(request,'contact.html')

def index(request):
    return render(request,'index.html')

def login(request ):
    if request.method == 'POST':


        user_id=request.POST.get("name")
        password=request.POST.get("password")
        context={}


    return render(request,'login.html')

def sucess(request):
    return render(request,'sucess.html')

def index(request):
    return render(request,'index.html')

def welcomepage(request):
    return render(request,'welcomepage.html')