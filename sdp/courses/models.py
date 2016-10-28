# Change log
# AK - responsible for change 1
#

from django.db import models

# Create your models here.
# change 1 -
from staff.models import Participant
# from staff.models import Participant, Instructor


class Course(models.Model):
	# change 1 - 
	instructor = models.CharField(max_length=20)
	# instructor = models.ForeignKey(Instructor, on_delete= models.CASCADE)
	courseCode = models.CharField(max_length=200)
	category  = models.CharField(max_length=200)
	isPublished = models.BooleanField(default=False)
	title = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.courseCode+' '+ ' '+ self.title +' '+ self.category+' Published: '+ str(self.isPublished)

	# def Course(self, category, title, code, description):
	# 	pass
	# def addModule(self, module):
	# 	pass
	# def publishCourse(self):
	# 	pass

class Module(models.Model):
	# change 1
	courseCode = models.CharField(max_length=20)
	# courseCode = models.ForeignKey(Course, on_delete=models.CASCADE)
	moduleTitle = models.CharField(max_length=200)
	sequenceNumber = models.IntegerField()

	def __str__(self):
		return 'CourseID: ' + self.course_id+' SequenceNo: '+ self.sequenceNumber

class Component(models.Model):
	# change 1
	courseCode = models.CharField(max_length=20)
	moduleTitle = models.CharField(max_length=200)
	# module = models.ForeignKey(Module, on_delete=models.CASCADE)
	order = models.IntegerField()
	contentType = models.CharField(max_length=200)
	content = models.TextField()
	contentTitle = models.CharField(max_length=200)

	def __str__(self):
		return 'Module: '+ self.module_id+', order: '+ self.order


class Enrollment(models.Model):
	isCompleted = models.BooleanField(default=False)
	# change 1
	courseCode = models.CharField(max_length=20)
	# course = models.ForeignKey(Course, on_delete= models.CASCADE)
	# change 1
	participant = models.CharField(max_length=20)
	# participant = models.ForeignKey(Participant, on_delete = models.CASCADE)


	def __str__(self):
		return 'Course: '+self.course_id+", Participant: "+ self.participant_id+', completed: '+ self.isCompleted