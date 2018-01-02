from django.db import models

# Create your models here.
class Task(models.Model):
	taskId = models.AutoField(max_length=10,primary_key=True,serialize=True)
	taskName = models.CharField(max_length=20)
	isDone = models.NullBooleanField(default=True)
	createdAt = models.DateTimeField(null=True)
	doneAt = models.DateTimeField(null=True)

	def __str__(self):
		return taskId,taskName,isDone,createdAt,doneAt