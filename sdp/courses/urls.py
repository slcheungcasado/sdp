from django.conf.urls import url, include
from . import views


app_name = 'courses'

urlpatterns = [
	#courses/
    url(r'^$', views.index, name='index'),
    #/courses/71/
    url(r'^(?P<course_id>[0-9]+)/$', views.courseDescription, name='courseDescription'),
    #/courses/71/enroll
    url(r'^(?P<course_id>[0-9]+)/enroll/$', views.enroll, name='enroll'),
    #/courses/71/addModule
    url(r'^(?P<course_id>[0-9]+)/addModule/$', views.addModule, name='addModule'),
    #/courses/71/modules/12/addComponent
    url(r'^(?P<course_id>[0-9]+)/modules/(?P<module_id>[0-9]+)/addComponent/$', views.addComponent, name='addComponent')
 
]