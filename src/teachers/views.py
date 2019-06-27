from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
# from rest_framework import authentication, permissions
# from django.contrib.auth.models import User

# Create your views here.
class ListTeachers(ListAPIView):
	serializer_class = TeacherSerializer
	queryset = Teacher.objects.filter(active=True)

class CreateTeacher(CreateAPIView):
	serializer_class = TeacherSerializer