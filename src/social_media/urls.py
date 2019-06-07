from django.urls import path
from .views import index_media, facebook, twit

urlpatterns = [
	path('', index_media),
	path('facebook', facebook),
	path('twitter/post', twit),
]