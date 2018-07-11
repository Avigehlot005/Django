from django.shortcuts import render,redirect
from catalog.models import Testing,Testing2
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def index(request):
	name=request.POST.get('Name')
	email=request.POST.get('Email')
	number=request.POST.get('Number')
	date=request.POST.get('date')
	message=request.POST.get('message')
	testing=Testing(name=name,email=email,number=number,date=date,message=message)
	testing.save()
	name=request.POST.get('First Name')
	last=request.POST.get('Last Name')
	email=request.POST.get('Email')
	subject=request.POST.get('Subject')
	message=request.POST.get('Message')
	a=Testing2(name=name,last=last,email=email,subject=subject,message=message)
	a.save()
	return render(request,'catalog/index.html')


	
	




 
 	

