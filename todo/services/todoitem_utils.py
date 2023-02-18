from todo.models import TodoItem


class TodoitemUtil:

    def get_todo_item_details(self, todo_item_id, user):
        try:
            todo_item = TodoItem.objects.get(id=todo_item_id, user_id=user.id)
        except TodoItem.DoesNotExist:
            return None, "Todo Item not found!"
        return todo_item, None
    
    def create_todo_item(self, user, name, description=None):
        todo_item = TodoItem.objects.create(
            name=name,
            description=description,
            user=user
        )
        return todo_item, None
        

    def edit_todo_item(self, user, todo_item_id, name=None, description=None):
        todo_item, error = self.get_todo_item_details(todo_item_id=todo_item_id, user=user)
        if error:
            return None, error

        if name:
            todo_item.name = name
        if description:
            todo_item.description = description
        todo_item.save()
        return todo_item, None
    
    def list_todo_items(self, user):
        return TodoItem.objects.filter(user_id=user.id).order_by('-created_at')

    def delete_todo_item(self, todo_item_id, user):
        # Todo mark the item inactive rather than deleting it
        todo_item, error = self.get_todo_item_details(todo_item_id=todo_item_id, user=user)
        if error:
            return None, error
        
        todo_item.delete()
        return True, None

    def mark_todo_item_completed(self, todo_item_id, user):
        todo_item, error = self.get_todo_item_details(todo_item_id=todo_item_id, user=user)
        if error:
            return None, error
            
        todo_item.is_completed = True
        todo_item.save()
        return todo_item, None
