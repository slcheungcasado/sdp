from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import JsonResponse

from .models import Module, Course, Enrollment, Component
from staff.models import Instructor, Participant

# Create your views here.

def index(request):
	# View all courses
	# courses = Course.objects.all().filter(isPublished = True)
	# return render(request, 'courses/courses.html', {'courses': courses})
	courses = Course.objects.all()
	coursesData = serializers.serialize('json', courses)
	return JsonResponse(coursesData, safe=False)

def addCourse(request):

	# Sourav -> Verify if courseCode already exits, return failure if true

	course = Course(
		instructor = request.GET['instructor'],
		courseCode = request.GET['courseCode'],
		category  = request.GET['category'],
		isPublished = request.GET['isPublished'],
		title = request.GET['title'],
		description = request.GET['description'])
	course.save()

	courses = Course.objects.all()
	# courses = Course.objects.all().filter(courseCode = request.GET['courseCode'])[:1]
	# courses = Course.objects.all().filter(isPublished = True)
	coursesData = serializers.serialize('json', courses)
	return JsonResponse(coursesData, safe=False)

def addModule(request, course_id):

	# # err if course does not exist
	# try:
	# 	course = Course.objects.get(pk = course_id)
	# except Course.DoesNotExist:
	# 	return render(request, 'courses/err.html', {'message': 'Course does not exist'})

	# ## POST request
	# ## Instructor id provided as post params. Check if course is created by course instructor
	# try: 
	# 	instructor = Instructor.objects.get(pk = request.POST['insID'])
	# except Instructor.DoesNotExist:
	# 	## display appropriate error message with authorization fails
	# 	return render(request, 'courses/err.html', {'message': "Instructor with the ID does not exits"})

	# isCourseInstructor = course.instructor == instructor.id

	# if isCourseInstructor == False:
	# 	return render(request, 'courses/err.html', {'message': 'You are not allowed to add modules to the course'})

	# components = request.POST['components']
	# module = Module.components_set.create(components)
	# module.sequenceNumber = request.POST['sequenceNumber']
	# module.course = course_id

	# return render(request, 'courses/modules.html', {'module': module, 'isInstructor': isInstructor})

	# Sourav -> Verify if courseCode exits, continue only if true

	module = Module(
		courseCode = course_id,
		moduleTitle = request.GET['moduleTitle'],
		sequenceNumber = request.GET['sequenceNumber'])
	module.save()

	modules = Module.objects.all().filter(courseCode = course_id).order_by('sequenceNumber')
	modulesData = serializers.serialize('json', modules)
	return JsonResponse(modulesData, safe=False)

def addComponent(request, course_id, module_id):
	
	# try:
	# 	course = Course.objects.get(pk = course_id)
	# except Course.DoesNotExist:
	# 	return render(request, 'courses/err.html', {'message': 'Course does not exit'})


	# ## POST request
	# ## Instructor id provided as post params. Check if course is created by course instructor
	# try: 
	# 	instructor = Instructor.objects.get(pk = request.POST['insID'])
	# except Instructor.DoesNotExist:
	# 	## display appropriate error message with authorization fails
	# 	return render(request, 'courses/err.html', {'message': "Instructor with the ID does not exits"})

	# isCourseInstructor = course.instructor == instructor.id

	# if isCourseInstructor == False:
	# 	return render(request, 'courses/err.html', {'message': 'You are not allowed to add modules to the course'})


	# ## get module. Display err if module not present
	# try:
	# 	module = Module.objects.get(pk = module_id)
	# except Module.DoesNotExist:
	# 	return render(request, 'courses/err.html', {'message': 'Module does not '})

	# component = Component(module=module_id,order =request.POST['order'], 
	# 	contentType=request.POST['contentType'], content=request.POST['content'])
	# component.save()

	# return render(request, 'courses/module_details.html', {'module': module})

	# Sourav -> Verify if courseCode and moudule exits, continue only if true

	component = Component(
		courseCode = course_id,
		moduleTitle = module_id,
		order = request.GET['order'], 
		contentType = request.GET['contentType'],
		content = request.GET['content'],
		contentTitle = request.GET['contentTitle'])
	component.save()

	components = Component.objects.all().filter(courseCode = course_id).filter(moduleTitle = module_id).order_by('order')
	componentsData = serializers.serialize('json', components)
	return JsonResponse(componentsData, safe=False)

def publishCourse(request, course_id):
	## POST request
	## Instructor id provided as post params. Check if course is created by course instructor
	try: 
		instructor = Instructor.objects.get(pk = request.POST['insID'])
	except Instructor.DoesNotExist:
		## display appropriate error message with authorization fails
		return render(request, 'courses/err.html', {'message': "Instructor with the ID does not exits"})


	## appropriate error message if course does not exist
	try:
		course = Course.objects.get(pk = course_id)
	except Course.DoesNotExist:
		return render(request, 'courses/err.html', {'message': 'Course does not exit'})

	course.isPublished = True
	course.save()
	return render(request, 'courses/course_details.html', {'course': course})

def courseDescription(request, course_id):
	# course = get_object_or_404(Course, pk = course_id)
	# ## Instructor id provided as get params. Check if course is created by course instructor
	# try: 
	# 	instructor = Instructor.objects.get(pk = request.GET['insID'])
	# except Instructor.DoesNotExist:
	# 	## display appropriate error message with authorization fails
	# 	return render(request, 'courses/err.html', {'message': "Instructor with the ID does not exits"})

	# isCourseInstructor = course.instructor == instructor.id 
	# ## show appropriate course description page depending on whether participant or instructor
	# return render(request, 'courses/course_description.html', {'course': course, 'isCourseInstructor': isCourseInstructor})
	course = Course.objects.all().filter(courseCode = course_id)
	courseData = serializers.serialize('json', course)
	return JsonResponse(courseData, safe=False)

def enroll(request, course_id):
	# ##POST request
	# #check if parID specified exist
	# try:
	# 	participant = Participant.objects.get(pk = request.POST['parID'])
	# except Participant.DoesNotExist:
	# 	# err if participant does not exist
	# 	return render(request, 'courses/err.html', {'message': 'Participant with the id does not exist'})

	# # err if course does not exist
	# try:
	# 	course = Course.objects.get(pk = course_id)
	# except Course.DoesNotExist:
	# 	return render(request, 'courses/err.html', {'message': 'Course does not exit'})

	# enroll = Enrollment(course=course_id, participant_id=participant.id)
	# return render(request, 'staff/course_description.html', {'course': course})

	enrollment = Enrollment(
		isCompleted = False,
		courseCode = course_id,
		participant = request.GET['participant'])
	enrollment.save()

	enrollments = Enrollment.objects.all()
	enrollmentsData = serializers.serialize('json', enrollments)
	return JsonResponse(enrollmentsData, safe=False)