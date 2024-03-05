from django.shortcuts import render,redirect
from dest.models import location,place,Hotels
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    l=location.objects.all()
    h=Hotels.objects.all()
    return render(request,'home.html',{'loc':l,'hot':h})
# Create your views here.
def details(request,p):
    l=location.objects.get(dname=p)
    k=place.objects.filter(locate=l)
    h=Hotels.objects.get(place=p)
    return render(request,'details.html',{'loc':l,'plc':k,'hot':h})


def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        c=request.POST['q']
        e=request.POST['e']

        if p==c:
            u=User.objects.create_user(username=u,password=p,email=e)
            u.save()
            return render(request,'login.html')
        else:
            return HttpResponse("Password not matching")

    return render(request,'register.html')

def user_login(request):
    if request.method=="POST":
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('dest:home')

        else:
            messages.error(request,"Invalid credentials")
    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return user_login(request)

