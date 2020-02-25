from django.urls import path,include
from todo_list.views import Alltasks, specifictask
from todo_list.views import finish, delete,add

urlpatterns = (
    path('', Alltasks.as_view(), name='home'),
    path('task/<int:pk>/', specifictask.as_view(), name='detailed'),
    path('task/<int:pk>/finish/', finish, name='finish'),
    path('task/<int:pk>/delete/', delete, name='delete'),
    path('task/add/', add, name='add')

)