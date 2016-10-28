from django.shortcuts import render

# from django.shortcuts import render, get_object_or_404
# from django.core import serializers
# from django.http import JsonResponse

# from .models import Instructor, Participant
# from courses.models import Module, Course, Enrollment, Component

def instructor(request):
	return render(request, 'staff/instructor.html')

def participant(request):
	return render(request, 'staff/participant.html')