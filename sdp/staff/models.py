from django.db import models

# Create your models here.

class Staff(models.Model):
	username = models.CharField(max_length=8)
	password = models.CharField(max_length=200)




class Participant(Staff):

	def Participant(self, username, password):
		pass
	def isCourseCompleted(self, courseCode):
		pass
	def enroll(self, couseCode):
		pass
	def getTakenCourses(self):
		pass

class Instructor(Staff):
	def Instructor(self, username, password):
		pass
	def createCourse(self, course):
		pass
	def getCourse(self, courseCode):
		pass

