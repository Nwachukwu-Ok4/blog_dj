from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def userLogin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, "user/signin.html", {"form" : form})



def userSignup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = UserCreationForm()
    return render(request, "user/signup.html", {"form" : form})


def userLogout(request):
    if request.method == "POST":
        logout(request)
        return redirect('userLogin')




