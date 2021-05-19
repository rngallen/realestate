from django.shortcuts import render, redirect
from pages.models import Company, SocialNetwork
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def userlogin(request):
    if request.method == "POST":
        username = request.POST["username"].lower()
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back {username}")
            return redirect("estate:dashboard")
        else:
            if User.objects.filter(username=username).exists():
                messages.error(
                    request, f"Wrong password for the user {request.POST['username']}"
                )
            else:
                messages.error(request, f"Username {username} does not exists!")
    try:
        # company = Company.objects.all()[:1].get()
        company = Company.objects.first()
        # social = SocialNetwork.objects.all()[:1].get()
        social = SocialNetwork.objects.first()
    except:
        company = []
        social = []
    context = {
        "company": company,
        "social": social,
        "values": request.POST,
    }
    return render(request, "accounts/login.html", context)


def userregister(request):
    try:
        company = Company.objects.all()[:1].get()
        social = SocialNetwork.objects.all()[:1].get()
    except:
        pass
    if request.method == "POST":
        fname = request.POST["first_name"]
        lname = request.POST["last_name"]
        username = request.POST["username"].lower()
        email = request.POST["email"].lower()
        password1 = request.POST["password"]
        password2 = request.POST["password2"]
        # Check for password
        if password1 == password2:
            # check for existing username
            if User.objects.filter(username=username).exists():
                messages.error(
                    request, f"Username {request.POST['username']} already exists!"
                )
            else:
                # Check for existing email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f"{email} alreay taken!")
                else:
                    # create user to the model
                    user = User.objects.create_user(
                        username=username,
                        first_name=fname,
                        last_name=lname,
                        email=email,
                        password=password1,
                    )
                    messages.success(
                        request,
                        f"Hello {username} your acccount has been created successfully!",
                    )
                    # authenticate created user
                    user = authenticate(request, username=username, password=password1)
                    # login authenticated user
                    if user is not None:
                        login(request, user)
                        return redirect("estate:dashboard")
        else:
            messages.error(request, f"Password mismatch!")
    context = {
        "company": company,
        "social": social,
        "values": request.POST,
    }
    return render(request, "accounts/register.html", context)


def userlogout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, f"You have logout!!")
        return redirect("pages:index")
