from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
import json
from . import models
from django.core import serializers

def index(request):
	tasks=models.Task.objects.all()
	data = [{'taskID':t.taskId,
	'taskName':t.taskName,
	'isDone': t.isDone,
	'createdAt':t.createdAt,
	'doneAt':t.doneAt} for t in tasks]
	return JsonResponse(data,safe=False)

class addTask(View):
	def get(self, request):
		return render(request,'post-task.html')
	def post(self, request):
		task = models.Task(taskName=request.POST['taskName'])
		if request.POST['taskName']:
			task.taskName=request.POST['taskName']
		if request.POST['createdAt']:
			task.createdAt=request.POST['createdAt']
		if request.POST['doneAt']:
			task.isDone=True
			task.doneAt=request.POST['doneAt']
		else:
			task.isDone=False
		task.save()
		data = {'taskId':task.taskId,
		'taskName':task.taskName,
		'isDone':task.isDone,
		'createdAt':task.createdAt,
		'doneAt':task.doneAt}
		return JsonResponse(data,safe=False)

def getTaskById(request,taskId):
	task = models.Task.objects.get(taskId=taskId)
	data = {'taskId':taskId,
	'taskName':task.taskName,
	'isDone':task.isDone,
	'createdAt':task.createdAt,
	'doneAt':task.doneAt}
	return JsonResponse(data,safe=False)

class updateTask(View):
	def get(self,request,taskId):
		return render(request,'post-task.html')
	def post(self, request,taskId):
		task = models.Task.objects.get(taskId=taskId)
		if request.POST['taskName']:
			task.taskName=request.POST['taskName']
		if request.POST['createdAt']:
			task.createdAt=request.POST['createdAt']
		if request.POST['doneAt']:
			task.isDone=True
			task.doneAt=request.POST['doneAt']
		task.save()
		data = {'taskId':task.taskId,
		'taskName':task.taskName,
		'isDone':task.isDone,
		'createdAt':task.createdAt,
		'doneAt':task.doneAt}
		return JsonResponse(data,safe=False)