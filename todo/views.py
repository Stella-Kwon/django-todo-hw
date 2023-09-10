from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from todo.models import Todo
from users.models import UserModel


# Create your views here.
@csrf_exempt
def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            todo = Todo.objects.create(
                context=request.POST['contents'],
                title=request.POST['title'],
                image=request.FILES.get('image'),
                author=request.user)
            return redirect("/todo/")
        elif request.method == "GET":
            return render(request, 'todo/create.html')
        else: 
            return HttpResponse("Invalid request method", status=405)
    else:
        login_url = f"/users/login/?next={request.path}"
        return redirect (login_url)

def list(request):
    if request.method == "GET":
        todo = Todo.objects.all() 
        request.method == "GET"
        context = {
                "todo" : todo,
            }
        return render(request, "todo/list.html", context)
    # elif request.method =="POST":
        #checkpoint용 
    else:
        return HttpResponse("invalid request method", status = 405)

def detail_read(request, todo_id):
    if request.method == "GET":
        todo = Todo.objects.get(id = todo_id)
        context = {
            'todo' : todo,
        }
        return render(request,'todo/details.html',context)
    else:
        return HttpResponse("invalid request method", status = 405)
    
    
def delete(request, todo_id):
    if request.method == "POST":
        todo = Todo.objects.get(id=todo_id)
        if request.user == todo.author:
            todo.delete()
            return redirect("/todo/")
        else:
            return HttpResponse("You have no rights to delete this context", status=403)
    else:
        return HttpResponse("Invalid request method",status = 405)
    
def edit(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    if request.method == "POST":
        if request.user.is_authenticated and request.user == todo.author:
            title = request.POST['title']
            context = request.POST['context']
            image = request.FILES.get('image')
            todo.save()
            messages.error(request,'수정 성공')
            return redirect(f'/todo/{todo.id}/')
        else:
            return HttpResponse("you don't have rights to edit this context",status=403)
    elif request.method == "GET":
        #{todo.id보내려면..... }
        
        return render (request,"todo/edit.html",{'todo':todo})
    else:
        return HttpResponse("Invalid request method", status=405)

def myposts(request):
    if request.user.is_authenticated:
        todos = Todo.objects.filter(author=request.user)
        if request.method == "GET":
            return render(request,'todo/myposts.html',{'todos':todos})
        else:
            return HttpResponse("Invalid request method", status=405)
    else:
        return HttpResponse("you don't have rights to edit this context",status=403)


def myprofile(request):
    # todo = Todo.objects.all()
    # if request.user.is_authenticated:
        if request.method =="GET":
            return render(request,'todo/myprofile.html')#,{'todos':todos})
        
        # elif request.method == "POST":
        #     pass