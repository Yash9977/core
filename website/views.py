from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    
    queryset=destination.objects.all()
    print(queryset)
    return render(request,"index.html",context={"data":queryset})

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def destinations(request):
    token=request.GET.get('token')
    print(token)
    try:
        session.objects.get(token=token)
    except:
        print("session not found ")    
    return render(request,"destinations.html")

def login(request):
    if request.method =="POST":
        
        username=request.POST.get('username')
        password=request.POST.get('password')
        print( 
                username,
                password,
        )
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                ses=session.objects.create(user=user,token=session.create_token(username))
                ses.save()
                print("Password has been  successfully.")
                return render(request,"destinations.html",context={'token':ses.token})
        except User.DoesNotExist:
            print("No user found with the given username.")
            return redirect('/signup')
    return render(request,"login.html")
            
 
def signup(request):
    if request.method =="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        print( first_name,
                last_name,
                username,
                password,
        )
        user=User.objects.filter(username=username)
        user=User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        return redirect('/login')
    return render(request,"signup.html")
