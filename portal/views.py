from django.shortcuts import redirect, render


from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'home.html')
