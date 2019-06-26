from django.urls import path
from .views import MaterialUploadView, ListMaterialView

urlpatterns = [
	path('upload', MaterialUploadView.as_view()),
	path('list', ListMaterialView.as_view()),
]
