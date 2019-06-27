from django.urls import path
from .views import ListTeachers, CreateTeacher

urlpatterns = [
	path('list', ListTeachers.as_view()),
	path('create', CreateTeacher.as_view()),
]