from django.conf.urls import url, include
from . import views

app_name = 'courses'

urlpatterns = [
	#courses/
    url(r'^$', views.index, name='index'),
    
    #cources/addCourse
    url(r'^addCourse$', views.addCourse, name='addCourse'),
    #courses/71/addModule
    url(r'^(?P<course_id>.+)/addModule$', views.addModule, name='addModule'),
    #courses/71/modules/12/addComponent
    url(r'^(?P<course_id>.+)/modules/(?P<module_id>.+)/addComponent$', views.addComponent, name='addComponent'),
    
    #courses/71
    url(r'^(?P<course_id>.+)$', views.courseDescription, name='courseDescription'),
    #courses/71/enroll
    url(r'^(?P<course_id>.+)/enroll$', views.enroll, name='enroll'),
 
]