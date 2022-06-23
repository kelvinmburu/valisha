from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .emails import send_welcome_email
from valapp.models import Profile
from .forms import UpdateProfileForm

from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError


# Mailchimp Settings
api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID

# Create your views here.

# User login function
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

# User logout function
def logout_user(request):
    logout(request)
    return redirect('home')

# User register function
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

# Basic page navigation settings
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

# Profile section
def user_profile(request):
    profile = Profile.objects.get(owner=request.user)
    ctx = {'profile': profile,}
    return render(request, 'valapp/profile.html', ctx)

def update_profile(request):
    profile = Profile.objects.get(owner=request.user)
    form = UpdateProfileForm(instance=profile)
    if request.method == 'POST':
        form = UpdateProfileForm(
            request.POST, request.FILES, instance=profile )
        if form.is_valid():
            form.save()
            return redirect('profile')

    ctx = {'profile': profile, 'form': form}
    return render(request, 'valapp/update-profile.html', ctx)

# Subscription Logic
def subscribe(email):
    """
     Contains code handling the communication to the mailchimp api
     to create a contact/member in an audience/list.
    """

    mailchimp = Client()
    mailchimp.set_config({
        "api_key": api_key,
        "server": server,
    })

    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))

# Mailchimp function

def subscription(request):
    if request.method == "POST":
        email = request.POST['email']
        subscribe(email)
        messages.success(request, "Email received. thank You! ") # message

    return render(request, 'valapp/index.html')