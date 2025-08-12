from django.shortcuts import render,redirect
from .models import Profile

def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request,'login.html')





def CreateProfilePage(request):
    return render(request, "create.html")


def SaveProfileData(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        picture = request.FILES.get("picture")

        obj = Profile(name=name, email=email, phone=phone, picture=picture)
        obj.save()


        return redirect(CreateProfilePage)
