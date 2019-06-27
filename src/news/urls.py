from django.urls import path
from .views import ListNews, CreateNew

urlpatterns = [
	path('list', ListNews.as_view()),
	path('create', CreateNew.as_view()),
]