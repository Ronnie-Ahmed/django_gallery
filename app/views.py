from django.shortcuts import render,redirect
from .forms import loginform,registerform,PhotoForm,CategoryForm
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import PhotoGallery,PhotoCategory

# Create your views here.
@login_required(login_url='login')
def index(request):
    category=request.GET.get('category')
    categories=PhotoCategory.objects.all()
    
    if category is not None:
        photos=PhotoGallery.objects.filter(user=request.user,category__category__exact=category)
    elif category is None:
        photos=PhotoGallery.objects.filter(user=request.user)
        
    context={
        'photos':photos,
        'categories':categories
    }
    return render(request,"index.html",context)


@login_required(login_url='login')
def user_logout(request):
    auth.logout(request)
    return redirect('login')

def login(request):
    if request.method=='POST':
        form=loginform(request,request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            
            if user is not None:
                auth.login(request,user)
                return redirect('index')
    else:
        form=loginform()
        
    context={
        'form':form
    }             
    return render(request,"login.html",context)


def register(request):
    
    if request.method=='POST':
        form=registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            HttpResponse("Some Error Happened")
    else:
        form=registerform()
    context={
        'form':form
    }
    return render(request,'register.html',context)



@login_required(login_url='login')
def add(request):
    if request.method=='POST':
        form=PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            adduser=form.save(commit=False)
            adduser.user=request.user
            adduser.save()
            return redirect('index')
    else:
        form=PhotoForm()
    context={
        'form':form
    }    
    return render(request,'add.html',context)


@login_required(login_url='login')
def detailview(request,pk):
    photo=PhotoGallery.objects.get(id=pk)
    context={
        'photo':photo
    }
    return render(request,'detailview.html',context)
