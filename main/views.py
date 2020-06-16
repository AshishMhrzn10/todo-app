from django.shortcuts import render,HttpResponse,redirect
from django.utils import timezone
from main.models import Todo

# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    return render(request, 'home.html',{'todo_items':todo_items})

def add_todo(request):
    if request.method == 'POST':
        print(request.POST)
        date = timezone.now()
        content = request.POST['content']
        created_obj = Todo.objects.create(added_date=date, text=content)
        print(created_obj)

    return redirect(home)


def delete_todo(request,todo_id):
    if request.method == 'POST':
        Todo.objects.get(id=todo_id).delete()
    
    return redirect(home)
