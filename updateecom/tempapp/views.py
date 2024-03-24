from django.shortcuts import render,redirect
from.models import Product, Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.forms import SignUpForm
from django import forms



def category(request,foo):
	#Replace Hyphens with spaces

	foo=foo.replace('-',' ')
	#grab the category from the url
	try:
		#look up the category model
		category=Category.objects.get(name=foo)
		products=Product.objects.filter(category)
		return render(request,'apps/category.html', {'products':products,'category':category})

	except:
		messages.success(request,("that category doesn't exists"))
		return redirect('home')





def product(request,pk):
	product=Product.objects.get(id=pk)
	return render(request,'apps/product.html',{'product':product})



def myfunc(request):
	products=Product.objects.all()
	return render(request,'apps/home.html',{'p':products})

def about(request):
	return render(request,'apps/about.html')
def login_user(request):

	#return render(request,'apps/login.html')
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request, user)
			messages.success(request,("you have been login"))
			return redirect('home')
		else:
			messages.success(request,("please try again later"))
			return redirect('login')
	else:
		return render(request, 'apps/login.html')


def logout_user(request):
	logout(request)
	#return render(request,'apps/logout.html')
	messages.success(request,"you have been login")
	return redirect ('home')

'''def register_user(request):
	form=SignUpForm()
	if request.method=="POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			#log in user
			user=authenticate(username=username,password=password)
			login(request, user)
			messages.success(request,('you have registered'))
			return redirect('home')
		else:
			messages.success(request,('you  have not  registered'))
			return redirect('register')

	else:
		return render(request,'apps/register.html',{'form':form})'''
# from django.contrib.auth import authenticate, login
#from django.contrib import messages
#from django.shortcuts import render, redirect
#from .forms import SignUpForm

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']  # Use password1 since it's the first password field
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have registered successfully.')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'apps/register.html', {'form': form})


	


