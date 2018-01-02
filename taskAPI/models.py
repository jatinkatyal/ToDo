from django.db import models

# Create your models here.
class Task(models.Model):
	taskId = models.AutoField(max_length=10,primary_key=True,serialize=True)
	taskName = models.CharField(max_length=20)
	isDone = models.BooleanField(default=True,blank=True)
	createdAt = models.DateTimeField(null=True)
	doneAt = models.DateTimeField(null=True,blank=True)

	def __str__(self):
		return self.taskName