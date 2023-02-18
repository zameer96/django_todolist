import typing
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import TodoItem
from .services.todoitem_utils import TodoitemUtil


class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'todo_items'

    def get_queryset(self):
        return TodoItem.objects.all().order_by('-created_on')


class DetailView(generic.DetailView):
    model = TodoItem
    context_object_name = 'todo_item'
    template_name='todo/details.html'


def create_item_view(request):
    if request.POST:
        user = request.user
        name = request.POST.get('todo_name')
        description = request.POST.get('todo_description')
        context = {}
        todo_item, error = TodoitemUtil().create_todo_item(
            user=user, name=name,
            description=description
        )
        if error:
            context['error_message'] = 'Title is required for the item!'
        if not error:
            context['success_message'] = "Todo item added to the list!"
        return render(request, 'todo/create.html', context)
    else:
        return render(request, 'todo/create.html')