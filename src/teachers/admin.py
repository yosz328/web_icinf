from django.contrib import admin
from .models import Teacher

# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated', )
	list_display = ('first_name', 'last_name', 'email', )

admin.site.register(Teacher, TeacherAdmin)