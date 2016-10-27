from django.shortcuts import render, get_object_or_404

from .models import Module, Course, Enrollment, Component
from staff.models import Instructor, Participant

# Create your views here.


def index(request):
	#return all courses
	courses = Course.objects.all().filter(isPublished = True)
	return render(request, 'courses/courses.html', {'courses': courses})

def addCourse(request):
	course = Course(instructor = request.POST['instructor'], courseCode = request.POST['courseCode'], category  = request.POST['category'],
	isPublished = request.POST['isPublished'], title = request.POST['title'], description = request.POST['description'])
	course.save()

	return render(request, 'courses/addCourse.html')

def courseDescription(request, course_id):
	course = get_object_or_404(Course, pk = course_id)
	## Instructor id provided as get params. Check if course is created by course instructor
	try: 
		instructor = Instructor.objects.get(pk = request.GET['insID'])
	except Instructor.DoesNotExist:
		## display appropriate error message with authorization fails
		return render(request, 'courses/err.html', {'message': "Instructor with the ID does not exits"})

	isCourseInstructor = course.instructor == instructor.id 
	## show appropriate course description page depending on whether participant or instructor
	return render(request, 'courses/course_description.html', {'course': course, 'isCourseInstructor': isCourseInstructor})

def addModule(request, course_id):

	# err if course does not exist
	try:
		course = Course.objects.get(pk = course_id)
	except Course.DoesNotExist:
		return render(request, 'courses/err.html', {'message': 'Course does not exist'})

	## POST request
	## Instructor id provided as post params. Check if course is created by course instructor
	try: 
		instructor = Instructor.objects.get(pk = request.POST['insID'])
	except Instructor.DoesNotExist:
		## display appropriate error message with authorization fails
		return render(request, 'courses/err.html', {'message': "Instructor with the ID does not exits"})

	isCourseInstructor = course.instructor == instructor.id

	if isCourseInstructor == False:
		return render(request, 'courses/err.html', {'message': 'You are not allowed to add modules to the course'})

	components = request.POST['components']
	module = Module.components_set.create(components)
	module.sequenceNumber = request.POST['sequenceNumber']
	module.course = course_id

	return render(request, 'courses/modules.html', {'module': module, 'isInstructor': isInstructor})

def addComponent(request, course_id, module_id):
	try:
		course = Course.objects.get(pk = course_id)
	except Course.DoesNotExist:
		return render(request, 'courses/err.html', {'message': 'Course does not exit'})


	## POST request
	## Instructor id provided as post params. Check if course is created by course instructor
	try: 
		instructor = Instructor.objects.get(pk = request.POST['insID'])
	except Instructor.DoesNotExist:
		## display appropriate error message with authorization fails
		return render(request, 'courses/err.html', {'message': "Instructor with the ID does not exits"})

	isCourseInstructor = course.instructor == instructor.id

	if isCourseInstructor == False:
		return render(request, 'courses/err.html', {'message': 'You are not allowed to add modules to the course'})


	## get module. Display err if module not present
	try:
		module = Module.objects.get(pk = module_id)
	except Module.DoesNotExist:
		return render(request, 'courses/err.html', {'message': 'Module does not '})

	component = Component(module=module_id,order =request.POST['order'], 
		contentType=request.POST['contentType'], content=request.POST['content'])
	component.save()

	return render(request, 'courses/module_details.html', {'module': module})

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

def enroll(request, course_id):
	##POST request
	#check if parID specified exist
	try:
		participant = Participant.objects.get(pk = request.POST['parID'])
	except Participant.DoesNotExist:
		# err if participant does not exist
		return render(request, 'courses/err.html', {'message': 'Participant with the id does not exist'})

	# err if course does not exist
	try:
		course = Course.objects.get(pk = course_id)
	except Course.DoesNotExist:
		return render(request, 'courses/err.html', {'message': 'Course does not exit'})

	enroll = Enrollment(course=course_id, participant_id=participant.id)
	return render(request, 'staff/course_description.html', {'course': course})