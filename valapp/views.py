from django.shortcuts import render

# Create your views here.
def home(request):
    text = 'Hello django'
    context = {
        'text': text,
    }
    return render(request, 'valapp/index.html', context)
