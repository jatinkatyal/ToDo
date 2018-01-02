from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add',views.addTask.as_view(),name='addTask')
    path('update/<int:taskId>',views.task.as_view,name='task')
]

