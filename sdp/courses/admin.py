from django.contrib import admin

# Register your models here.
from .models import Course, Module, Component, Enrollment

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Component)
admin.site.register(Enrollment)
