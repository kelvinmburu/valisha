from django.shortcuts import render

# Create your views here.
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
