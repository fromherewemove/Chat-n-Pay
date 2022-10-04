import email
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from account.models import CustomUser
# Create your views here.

def signup(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        password = request.POST["password"]
        email = request.POST["email"]
        date_of_birth = request.POST["dob"]
        bvn = request.POST["bvn"]
        user = authenticate(request, email=email, password=password)

        if user is None:
            user = User.objects.create_user(username=first_name + " " + last_name ,first_name=first_name, last_name=last_name, password=password, email=email)
            custom_user = CustomUser.objects.create(user=user, date_of_birth=date_of_birth, bvn=bvn)
            user.save()
            custom_user.save()

    return render(request, 'account/signup.html')