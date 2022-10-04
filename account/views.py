from django.shortcuts import render, redirect
from .forms import *
from django.views import *
# Create your views here.

def register(request):
    form = UserRegistration(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_user = form.save()
            return redirect('account:register')
    return render(request, "account/register.html", context = {"form":form})