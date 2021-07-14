import datetime
import json
import os

#import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render,redirect
from django.urls import reverse

from accounts.EmailBackEnd import EmailBackEnd
from accounts.models import CustomUser
from config import settings

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# secret   6LeTfBYbAAAAAEAWPUEu_ANiR1mmXjhHc21uQZPj
# site  6LeTfBYbAAAAAF4tBZTgcmMA3Gtp9kNFgejdEFDk

@login_required
def showDemoPage(request):
    return render(request,"demo.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:

        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect('/admin_home')
            elif user.user_type=="2":
                return HttpResponseRedirect("/member_home")
            
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")


def ShowLoginPage(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login_page.html", context={"login_form":form})


# @login_required
# def doLogin(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			email = form.cleaned_data.get('email')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(email=email, password=password)
# 			if user is not None:
# 				login(request,user)
# 				messages.info(request, f"You are now logged in as {email}.")
# 				return redirect("home")
# 			else:
# 				messages.error(request,"Invalid email or password.")
# 		else:
# 			messages.error(request,"Invalid email or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="login_page.html", context={"login_form":form})

@login_required
def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")

# def signup_member(request):
#     return render(request,"signup_member_page.html")

# def do_member_signup(request):
#     username=request.POST.get("username")
#     email=request.POST.get("email")
#     password=request.POST.get("password")


#     try:
#         user=CustomUser.objects.create_user(username=username,password=password,email=email,user_type=2)
#         user.save()
#         messages.success(request,"Successfully Created Member")
#         return HttpResponseRedirect(reverse("ShowLoginPage"))
#     except:
#         messages.error(request,"Failed to Create Member")
#         return HttpResponseRedirect("/")

def do_member_signup(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		# first_name = request.POST.get('first_name')
		# last_name = request.POST.get('last_name')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		if password1 == password2:
			if User.objects.filter(username=username).exists():
				messages.info(request, 'Username has been taken')
				return redirect('signup')
			elif User.objects.filter(email=email).exists():
				messages.info(request, 'Email already exists')
				return redirect('login')
			else:
				user = User.objects.create_user(username=username, email=email, password=password1)
				user.save()
				messages.success(request, 'Congrats for signing up!')
				return redirect('login')
		else:
			messages.info(request, 'password does not match')
			return redirect('login')
	else:
		return render(request,'login_page.html',{'title':'signup'})

