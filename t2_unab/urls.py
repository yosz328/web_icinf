"""t2_unab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='ICF UNAB API')

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('src.base.urls')),
	path('rrss/', include('src.social_media.urls')),
	path('news/', include('src.news.urls')),
	path('teachers/', include('src.teachers.urls')),
   	path('material/', include('src.support_material.urls')),
	path('docs/', schema_view),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
