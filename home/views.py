from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from . models import Note
from . models import UploadImage


# from . models import Records
# Create your views here.
def dashboard(request):
    user = request.user 
    return render(request,"dashboard.html")

def Invalid(request):
    return render(request,"Invalid.html")

def login1(request):
    if request.method == "POST":
        username = request.POST.get("username")
        userpass = request.POST.get("userpass")
        user = authenticate(request,username = username,password = userpass)
        if user is not None:
            login(request, user)
            return redirect("YourPost")
        else:
            return redirect("login1")
    return render(request,"login1.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        uemail = request.POST.get("uemail")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        userpass = request.POST.get("userpass")
        re_enter = request.POST.get("re_enter")
        myuse = User.objects.create_user(username = username,email = uemail,first_name = fname,last_name = lname)
        myuse.set_password(userpass)
        if userpass == re_enter:
            myuse.save()
            return redirect("YourPost")
        else:
            return redirect("login1")

    return render(request,"login1.html")

def Business(request):
    # if request.method == "POST":
    #     bname = request.POST.get("bname")
    #     bpass = request.POST.get("bpass")
    #     buser = authenticate(request,username = bname,password = bpass)
    #     if buser is not None:
    #         login(request, buser)
    #         return redirect("BusinessPage")
    #     else:
    #         return redirect("Business")
    return render(request,"Business.html")

# def register(request):
#     if request.method == "POST":
#         na = request.POST.get("na")
#         em = request.POST.get("em")
#         pa = request.POST.get("pa")
#         co = request.POST.get("co")
#         myus = User.objects.create_user(username = na,email = em)
#         myus.set_password(pa)
#         if userpass == co:
#             myus.save()
#             return redirect("BusinessPage")
#         else:
#             return redirect("Business")

#     return render(request,"Business.html")


def BusinessPage(request):
    return render(request,"BusinessPage.html")

def logout(request):
    logout(request)
    return render(request,"login1.html")

def index(request):
    if request.method == "POST":
        userr = request.POST.get("userr")
        uemail = request.POST.get("uemail")
        ucomment = request.POST.get("ucomment")
        new_note = Note.objects.create(userr = userr,uemail = uemail,ucomment = ucomment)
        new_note.save()
        return redirect("index")
    return render(request,"index.html")


@login_required(login_url="login1")
def community(request):
    if request.method == "POST":
        userr = request.POST.get("userr")
        uemail = request.POST.get("uemail")
        ucomment = request.POST.get("ucomment")
        new_note = Note.objects.create(userr = userr,uemail = uemail,ucomment = ucomment)
        new_note.save()
        return redirect("community")
    return render(request,"community.html")


@login_required(login_url="login1")
def Event(request):
    if request.method == "POST":
        userr = request.POST.get("userr")
        uemail = request.POST.get("uemail")
        ucomment = request.POST.get("ucomment")
        new_note = Note.objects.create(userr = userr,uemail = uemail,ucomment = ucomment)
        new_note.save()
        return redirect("Event")
    return render(request,"Event.html",{"user":request.user})

@login_required(login_url="login1")
def Profile(request):
    if request.method == "POST":
        userr = request.POST.get("userr")
        uemail = request.POST.get("uemail")
        ucomment = request.POST.get("ucomment")
        new_note = Note.objects.create(userr = userr,uemail = uemail,ucomment = ucomment)
        new_note.save()
        return redirect("Profile")
    # user = request.user
    # notes = Note.objects.all()
    # parameters = {
    #     "user":user,
    #     "notes":notes
    # }
    print(request.user)
    return render(request,"Profile.html",{"user":request.user})

@login_required(login_url="login1")
def Complain(request):
    if request.method == "POST":
        okmail = request.POST.get("okmail")
        addr = request.POST.get("addr")
        comment = request.POST.get("comment")
        num = request.POST.get("num")
        image = request.POST.get("image")
        new_feed = UploadImage.objects.create(okmail=okmail,addr=addr,comment=comment,num=num,image=image)
        new_feed.save()
        return redirect("YourPost")
    return render(request,"complain.html",{"user":request.user})

@login_required(login_url="login1")
def leaderboard(request):
    if request.method == "POST":
        userr = request.POST.get("userr")
        uemail = request.POST.get("uemail")
        ucomment = request.POST.get("ucomment")
        new_note = Note.objects.create(userr = userr,uemail = uemail,ucomment = ucomment)
        new_note.save()
        return redirect("leaderboard")
    return render(request,"Leaderboard.html",{"user":request.user})

@login_required(login_url="login1")
def Wallet(request):
    if request.method == "POST":
        userr = request.POST.get("userr")
        uemail = request.POST.get("uemail")
        ucomment = request.POST.get("ucomment")
        new_note = Note.objects.create(userr = userr,uemail = uemail,ucomment = ucomment)
        new_note.save()
        return redirect("Wallet")
    return render(request,"Wallet.html",{"user":request.user})

@login_required(login_url="login1")
def YourPost(request):
    if request.method == "POST":
        userr = request.POST.get("userr")
        uemail = request.POST.get("uemail")
        ucomment = request.POST.get("ucomment")
        new_note = Note.objects.create(userr = userr,uemail = uemail,ucomment = ucomment)
        new_note.save()
        return redirect("YourPost")
    return render(request,"YourPost.html",{"user":request.user})

@login_required(login_url="login1")
def CreatePost(request):
    if request.method == "POST":
        userr = request.POST.get("userr")
        uemail = request.POST.get("uemail")
        ucomment = request.POST.get("ucomment")
        new_note = Note.objects.create(userr = userr,uemail = uemail,ucomment = ucomment)
        new_note.save()
        return redirect("CreatePost")
    return render(request,"CreatePost.html",{"user":request.user})

@login_required(login_url="Business")
def Business(request):
    return render(request,"Business.html")

# def PopUp(request):
#     return render(request,"PopUp.html")

def Certificate(request):
    return render(request,"Certificate.html")