from django.shortcuts import render
from basic_app.forms import Userform,UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    registered=False

    if request.method=='POST':
        newUserFormObject=Userform(data=request.POST)
        newUserProfileInfoFormObject=UserProfileInfoForm(data=request.POST)

        if newUserFormObject.is_valid() and newUserProfileInfoFormObject.is_valid():
            new_user=newUserFormObject.save()
            new_user.set_password(new_user.password)
            new_user.save()

            profile=newUserProfileInfoFormObject.save(commit=False)
            profile.my_user=new_user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()
            registered=True
        else:
            print(newUserFormObject.errors,newUserProfileInfoFormObject.errors)
    else:
        newUserFormObject=Userform()
        newUserProfileInfoFormObject=UserProfileInfoForm()


    return render(request,'basic_app/register.html',{'user_form':newUserFormObject,'profile_form':newUserProfileInfoFormObject,'registered':registered})


def user_login(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("The user is not active")
        else:
            print("someone tried to login and failed!")
            print("username : {} and password : {}".format(username,password))
            return HttpResponse("Invalid login details")
    else:
        return render(request,'basic_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("This is the special fn which can be accessed only if u login") 

def index(request):
    return render(request,'basic_app/index.html')