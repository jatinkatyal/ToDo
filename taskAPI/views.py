from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
import json
from . import models
from django.core import serializers

def index(request):
	q=models.Task.objects.all()
	return JsonResponse(serializers.serialize('json',q.order_by('taskId')),safe=False)

class addTask(View):
	def get(self, request):
		return render(request,'add-task.html')
	def post(self, request):
		task = models.Task(taskName=request.POST['taskName'],
			isDone=request.POST['isDone'],createdAt=request.POST['createdAt'],
			doneAt=request.POST['doneAt'])
		task.save()
		return JsonResponse(request.POST)
class task(View):
	def get()
	