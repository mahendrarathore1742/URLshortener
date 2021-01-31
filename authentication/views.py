from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from .Form import Signupform
from django.contrib.auth import authenticate,login,logout;

def signup(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=Signupform(request.POST or None);

            if form.is_valid():
                form.save();
                return redirect("/login");
            else:
                messages.error(request,form.errors);
                return redirect("/signup");
        else:
            form=Signupform();
            return render(request,"signup.html",{"form":form});
        return render(request,'signup.html');
    else:
        return redirect("/deshbord");

def loginuser(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            if request.POST['email'] and  request.POST['password']:
                try:
                    user=User.objects.get(email=request.POST['email'])
                    auth.login(request,user)
                    if request.POST["next"] !="":
                        return redirect(request.POST.get('next'));
                    else:
                        return redirect("/");        
                    return redirect("/");
                except User.DoesNotExist:
                    messages.error(request,"User Does't Exist");

                    return render(request,"login.html");
            else:
                messages.error(request,"Empty field");
            
                return render(request,"login.html")
        else:
            return render(request,'login.html')
    else:
        return redirect("/deshbord");



def logoutuser(request):
    auth.logout(request);
    return redirect('/account/login') 
