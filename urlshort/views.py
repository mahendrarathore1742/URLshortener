from django.shortcuts import render,redirect
from django.contrib import messages
import random,string;
from .models import  Urls
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required;
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator



@login_required(login_url="/account/login/")
def deshbord(request):
    user=request.user
    urls=Urls.objects.filter(user=user).order_by('-id')
    return render(request,"Deshbord.html",{"urls":urls});

def randomgenerate():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(6));


def generate(request):
    if request.method=="POST":
        if request.POST['original'] and request.POST['short']:
            validator = URLValidator();

            try:
                validator(request.POST['original']);
            except ValidationError:
                messages.error(request,'Url is not valid');
                return redirect("/deshbord")

            user=request.user;
            original=request.POST["original"];
            short=request.POST['short'];
           
            checkurl=Urls.objects.filter(short_query=short);


            if not checkurl:
                newurl=Urls(
                    user=user,
                    oirignal_url=original,
                    short_query=short)

                newurl.save();
                return redirect('/deshbord');
            else:
                messages.error(request,"Already Shorted");
                return redirect("/deshbord");
            
        elif request.POST['original']:
            user=request.user;
            original=request.POST["original"];
            generated=False;
            validator = URLValidator();
            try:
                validator(request.POST['original']);
            except ValidationError:
                messages.error(request,'email is not valid');
                return redirect("/deshbord")

            while not generated:
                short=randomgenerate();
                checkurl=Urls.objects.filter(short_query=short);

                if not checkurl:
                    newurl=Urls(
                    user=user,
                    oirignal_url=original,
                    short_query=short)

                    newurl.save();
                    return redirect('/deshbord')
                else:
                    continue
        else:
            messages.error(request,'empty field');
            return redirect("/deshbord");
    else:
        return redirect("/deshbord");  
 
def Home(request,slug=None):
    if not slug or slug is None:
        return render(request,'index.html')
    else:
        try:
            check=Urls.objects.get(short_query=slug);
            check.visit=check.visit+1;
            check.save();
            url_to_redirect=check.oirignal_url;
            return redirect(url_to_redirect);
        except:
            messages.error(request,'Page Not Found');
            return redirect('/')

        
    return render(request,"index.html"); 





