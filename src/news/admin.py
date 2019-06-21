from django.contrib import admin
from .models import New

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated', )
	list_display = ('title', 'active', )

admin.site.register(New, NewsAdmin)