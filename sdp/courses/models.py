from django.db import models

# Create your models here.
from staff.models import Participant


class Course(models.Model):
	courseCode = models.CharField(max_length=200)
	category  = models.CharField(max_length=200)
	isPublished = models.BooleanField()
	title = models.CharField(max_length=200)
	description = models.TextField()

	def Course(self, category, title, code, description):
		pass
	def addModule(self, module):
		pass
	def publishCourse(self):
		pass



class Module(models.Model):
	course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
	sequenceNumber = models.IntegerField()

	def Module(self, sequenceNumber):
		pass
	def addComponent(self, module):
		pass

class Component(models.Model):
	module_id = models.ForeignKey(Module, on_delete=models.CASCADE)
	order = models.IntegerField()
	contentType = models.CharField(max_length=200)
	content = models.TextField() ##### 


	def Component(self, order, content, contentType):
		pass



class Enrollment(models.Model):
	isCompleted = models.BooleanField(default=False)
	course_id = models.ForeignKey(Course, on_delete= models.CASCADE)
	participant_id = models.ForeignKey(Participant, on_delete = models.CASCADE)

	def createEnrollment(self, courseCode, participantUsername):
		pass
