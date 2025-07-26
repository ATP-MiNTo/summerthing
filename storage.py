from typing import List, Optional
from models import Todo
from datetime import date

class TodoStorage:
    def __init__(self):
        self.todos: List[Todo] = []
        self.counter = 1

    def add_todo(self, item: str, due_date: date) -> Todo:
        todo = Todo(id=self.counter, item=item, due_date=due_date)
        self.todos.append(todo)
        self.counter += 1
        return todo

    def get_all(self) -> List[Todo]:
        return self.todos

    def get_upcoming(self) -> List[Todo]:
        today = date.today()
        return [todo for todo in self.todos if todo.due_date >= today]

    def delete_todo(self, todo_id: int) -> bool:
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                del self.todos[i]
                return True
        return False

    def edit_todo(self, todo_id: int, item: str, due_date: date) -> Optional[Todo]:
        for todo in self.todos:
            if todo.id == todo_id:
                todo.item = item
                todo.due_date = due_date
                return todo
        return None

storage = TodoStorage()
