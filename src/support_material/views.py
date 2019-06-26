from .serializers import MaterialSerializer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
# Create your views here.

class MaterialUploadView(CreateAPIView):
	serializer_class = MaterialSerializer