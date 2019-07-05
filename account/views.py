from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import UserRegisterForm
def home_view(request):
    return render(request,"testpages.html")

def user_logout(request):
    logout(request)
    return redirect('/')

def register(request):
    registered=False
    if request.method=='POST':
        user_form=UserRegisterForm(request.POST)
        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
            return redirect('/')
            
        else:
            print(user_form.errors)
    else:
        user_form=UserRegisterForm()
    return render(request,'auth/register.html',{'form':user_form,'registered':registered,'value':'Signup'})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect("/")
            else:
                return HttpResponse("Your account was inactive")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} password: {}".format(username,password))
            return HttpResponse("Invalid login detailes given")
    else:
        return render(request,'auth/login.html',{})

# Create your views here.
