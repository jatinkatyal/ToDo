from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add',views.addTask.as_view(),name='addTask'),
    path('<int:taskId>',views.getTaskById,name='task'),
    path('<int:taskId>/update',views.updateTask.as_view(),name='update')
]

