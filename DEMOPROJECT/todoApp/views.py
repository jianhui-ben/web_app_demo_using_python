from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import todoItem


def todoView(request):
    all_items = todoItem.objects.all()
    return render(request, 'todo.html',
                  {'all_items': all_items})

def addTodo(request):
    # create a new to-do item into all_items
    # save and redirect the browser to '/to-do'
    new_item = todoItem(content= request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/to-do/')


def deleteTodo(request, todo_id):
    delete_item = todoItem.objects.get(id=todo_id)
    delete_item.delete()
    return HttpResponseRedirect('/to-do/')


