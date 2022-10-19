from datetime import date, datetime
from multiprocessing import reduction
from django.shortcuts import redirect, render
from django.http import HttpResponse
from app.models import Contact, Regis
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == "POST":
        name=request.POST.get("name")
        kingdom=request.POST.get("kingdom")
        squad=request.POST.get("squad")
        help=request.POST.get("help")
        obj = Contact(name=name,kingdom=kingdom,squad=squad,help=help)
        obj.save()
        messages.success(request,"Submitted!!")
        return redirect('/#contact')
    return render(request,'index.html')

def registration(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        dob=request.POST.get("dob")
        gen=request.POST.get("gen")
        cnumb=request.POST.get("cnumb")
        reg = Regis(fname=fname,lname=lname,dob=dob,gen=gen,cnumb=cnumb)
        reg.save()
    return render(request,'registration.html')

def home1(request):
    return render(request,'index.html')