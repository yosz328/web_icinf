from django.urls import path
from .views import index_media, facebook

urlpatterns = [
    path('', index_media),
	path('facebook', facebook),
]