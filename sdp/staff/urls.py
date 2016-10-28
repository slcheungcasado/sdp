from django.conf.urls import url, include
from . import views

app_name = 'staff'

urlpatterns = [
    # Note: need to add <instructor_id> to allow multiple instructors
	# staff/instructor
    url(r'^instructor$', views.instructor, name='instructor'),

    # Note: need to add <participant_id> to allow multiple participants
    # staff/participant
    url(r'^participant$', views.participant, name='participant')
]