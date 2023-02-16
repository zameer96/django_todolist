from django.contrib import admin
from todo.models import TodoItem

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    pass
