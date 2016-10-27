from django.contrib import admin

# Register your models here.
from .models import Participant, Instructor

admin.site.register(Participant)
admin.site.register(Instructor)