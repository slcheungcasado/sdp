from django.db import models

# Create your models here.

class Staff(models.Model):
	username = models.CharField(max_length=8)
	password = models.CharField(max_length=200)


	def __str__(self):
		return self.username


class Participant(Staff):
	# def Participant(self, username, password):
	# 	pass
	# def isCourseCompleted(self, courseCode):
	# 	pass
	# def enroll(self, couseCode):
	# 	pass
	# def getTakenCourses(self):
	# 	pass
	pass

class Instructor(Staff):
	pass
	
