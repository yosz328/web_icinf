from django.urls import path
from .views import MaterialUploadView

urlpatterns = [
	path('upload', MaterialUploadView.as_view()),
]
