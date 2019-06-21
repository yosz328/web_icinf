from .models import New
from .serializers import NewSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
# from rest_framework import authentication, permissions
# from django.contrib.auth.models import User

# Create your views here.
class ListNews(ListAPIView):
	serializer_class = NewSerializer
	queryset = New.objects.filter(active=True)

class CreateNew(CreateAPIView):
	serializer_class = NewSerializer