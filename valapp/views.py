from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .emails import send_welcome_email
from valapp.models import Profile

# Create your views here.

def login_user(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')
    ctx = {'page': page}
    return render(request, 'valapp/auth.html', ctx)

def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            recipient = User(username=username, email=email)
            send_welcome_email(username, email)

            profile = Profile.objects.create(owner=user)
            profile.save()
            
            page = 'register'
            return render(request, 'valapp/success.html',{'page': page})
    ctx = {'form': form}
    return render(request, 'valapp/auth.html', ctx)

def home(request):
    context = {}
    return render(request, 'valapp/index.html', context)

def about(request):
    context = {}
    return render(request, 'valapp/aboutus.html', context)

def contact(request):
    context = {}
    return render(request, 'valapp/contact.html', context)

def causes(request):
    context = {}
    return render(request, 'valapp/causes.html', context)

def blog(request):
    context = {}
    return render(request, 'valapp/blog.html', context)

def contact(request):
    context = {}
    return render(request, 'valapp/contact.html', context)

