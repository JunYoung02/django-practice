from django.urls import path
from todo.views import TodoCreate, delete_todo, index, todos, update_todo, complete_todo

urlpatterns = [
	path('', todos, name="todo_list"),
	path('index/', index),
	path('create_todo/', TodoCreate.as_view(), name="create"),
	path('update_todo/<int:pk>/', update_todo, name='update'),
	path('delete_todo/<int:pk>/', delete_todo, name='delete'),
	path('complete_todo/<int:pk>/', complete_todo, name='complete'),
]