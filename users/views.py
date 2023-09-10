from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from users.models import UserModel

# Create your views here.

def signup(request):
    if request.method == "POST":
        raw_username = request.POST['username']
        username=raw_username.replace(" ","")
        email = request.POST['email']
        password = request.POST['password']
        if username and email and password:
            if UserModel.objects.filter(username=username).exists():
                messages.error(request, '이미 사용자가 있습니다. 다시 입력하여 주십쇼.')
                return redirect('/signup/')
            else:
                UserModel.objects.create_user(
                    username = username,
                    email = email,
                    password = password,
                )
                return render(request, 'users/login.html')
        else:
            error_message="아이디 비번 이메일 모두 채워주십시오."
            return render(request,'users/signup.html',{'error_message':error_message})
    elif request.method =="GET":
        return render(request,"users/signup.html")
    else: 
        return HttpResponse("Invalid request method", status=405)
        
def login(request):
    if request.method == "POST":
        username = request.POST['username'] 
        password = request.POST['password']
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request,user)
                next_url =request.POST.get('next','/todo/')
                return redirect(next_url)
            else:
                messages.error(request,'정보가 맞지 않습니다. 다시입력해 주십시오.')
                return redirect('/users/login/')
                
        else:
            messages.error(request,"아이디, 이메일과 비밀번호 모두 입력해 주십시오.")
            return redirect('/users/login/')
    elif request.method =="GET":
        return render(request,"users/login.html")
    else: 
        return HttpResponse("Invalid request method", status=405)
    
def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect('/todo/')
    else:
        return HttpResponse("Invalid request method", status=405)