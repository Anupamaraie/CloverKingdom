from datetime import date, datetime
from multiprocessing import reduction
from django.shortcuts import redirect, render
from django.http import HttpResponse
from app.models import Contact
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