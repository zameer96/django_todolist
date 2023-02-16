from django.db import models
from user.models import User

class TodoItem(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey('user.User', related_name='todo_item', on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    
    
