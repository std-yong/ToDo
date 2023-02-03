from django.shortcuts import render

from .models import ToDo
# Create your views here.
def todo_list(request):
    #완료되지 않은 항목 가져오기
    todos = ToDo.objects.filter(complete=False)
    return render(request, 'todo/todo_list.html',
                  {'todos': todos})

from .forms import ToDoForm
from django.shortcuts import redirect


def todo_post(request):
    if request.method == "GET":
        #Form을 만들어서 출력할 파일에 전달
        form = ToDoForm()
        return render(request, "todo/todo_post.html",
                      {"form": form})
    else:
        #데이터를 입력한 폼을 가져와서
        form = ToDoForm(request.POST)
        #폼의 데이터가 유효하면
        if form.is_valid():
            #폼에 입력한 데이터를 가지고 모델을 생성
            todo = form.save(commit=False)
            #모델을 데이터베이스에 추가
            todo.save()
            #데이터를 추가하고 todo_list로 이동
            return redirect('todo_list')


#pk 는 urls 에서 <> 안에 넘겨준 데이터이다
def todo_detail(request, pk):
    #pk에 해당하는 데이터 찾아오기
    todo = ToDo.objects.get(id=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})


def todo_edit(request, pk):
    #기본키에 해당하는 데이터 찾기
    todo = ToDo.objects.get(id=pk)
    if request.method ==  "GET":
        form = ToDoForm(instance=todo)
        return render(request, 'todo/todo_post.html',
                      {'form':form})
    else:
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect("todo_list")


def done_list(request):
    dones = ToDo.objects.filter(complete=True)
    return render(request, 'todo/done_list.html' , {'dones': dones})


def todo_done(request, pk):
    todo = ToDo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect('todo_list')
