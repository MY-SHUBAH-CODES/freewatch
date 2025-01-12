from pyexpat import model
from webbrowser import get
from django.shortcuts import render

# Create your views here.


from ast import Return
from contextlib import redirect_stderr
from django.http import HttpResponse
# from turtle import title
from urllib import response
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
# from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as li, logout as lo
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.shortcuts import render

from app1.admin import HomevidAdmin, MovievidAdmin
from .models import *
from django.contrib import auth

from django.core import serializers





# Create your views here.

@csrf_exempt
# =====================================================================================
# def login(request):
#     data = request.POST
#     user = authenticate(request, username=data.get("username"), password=data.get("password"))
#     response = {
#             "status":"error",
#             "message":"invalid credentials"
#     }
#     if user:
#         li(request,user)
#         response['status']="ok"
#         response['message']="User logged in successfully"
#     return JsonResponse(response)
def login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            li(request, user)
            # Success, now let's login the user.
            return render(request, 'movies.html')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'login.html')

# ============================================================================


def logout(request):
    try:
        lo(request)
        response = {
            "status": "ok",
            "message": "user logged Out"
        }
    except:

        response = {
            "status": "error",
            "message": "kya kr rhe ho yaar!!"
        }
    return JsonResponse(response)

#======================================================================================


def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password_again']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error_message': 'Username is already taken!'})
            except User.DoesNotExist:
                if len(request.POST['username']) < 5:
                    return render(request, 'signup.html', {'error_message': 'user name is too short'})

                if len(request.POST['password']) < 8:
                    return render(request, 'signup.html', {'error_message': 'password is too short'})

                else:
                    user = User.objects.create_user(request.POST['username'], request.POST['password'], request.POST['password_again'])
                # auth.login(request,user)
                    return render(request, 'login.html',{})
        else:
            return render(request, 'signup.html', {'error_message': 'Password does not match!'})
    else:
        return render(request, 'signup.html')

    # data = request.POST
    # print()
    # user = User.objects.create(**data)
    # return JsonResponse({"status":"ok","message":"user created successfully"})
    # # return render(request, 'login.html')


#========================================================================================

def changePassword(request):
    data = request.POST
    try:
        user = User.objects.get(username=data.get("username"))
    except:
        user = None
        response = {
            "status": "error",
            "message": "username not valid"
        }

    if user:

        user.set_password(data["password"])
        # user.password = make_password(data["password"])
        user.save()

#==========================================================================================

# def create_movie(request):
#     print("sdfsdfsdf")
#     Movie.objects.create(title="meramovie")
#     print(Movie)
#     return redirect("/")


# Create your views here.
@csrf_exempt
def home(request):
    obj=Home.objects.all()
    
    # for instance  in obj:
    #     data=instance.title
    #     vid=instance.video
    #     print(data,vid)
    # data = serializers.serialize( "python", Home.objects.all() )
    # print(data)



    

    # for i in obj:
    #     print(i.)
   
    # for i in obj:
    #     print(i.in)
    return render(request, 'home.html', {"obj": obj}) 
     #


# ===========================================================================================

def logout(request):
    try:
        lo(request)
        response = {
            "status": "ok",
            "message": "user logged Out"
        }
    except:

        response = {
            "status": "error",
            "message": "kya kr rhe ho yaar!!"
        }
    # return JsonResponse(response)
    return redirect('/')

# ================================================================================


def virals(request, path=None):
    obj=Viral.objects.all()
    return render(request, 'virals.html', {"obj": obj})

    # try:
    #     if User.is_authenticated:
    #         return render(request,'virals.html')
    # except:
    #     pass

    # =======================================================================


@csrf_exempt
def movies(request, path=None):
    obj = Movie.objects.all()
    return render(request, 'movies.html', {"obj": obj})
    # =======================================================================


def webshows(request):
    obj = Webshow.objects.all()
    return render(request, 'webshows.html', {"obj": obj})
    # =======================================================================


def shortfilms(request):
    obj = Shortfilm.objects.all()
    return render(request, 'shortfilms.html', {"obj": obj})
    # =======================================================================


def about(request):
    return render(request, 'about.html')
    # =======================================================================
