from django.db import models

# Create your models here.
class Schedule(models.Model):
	# TODO: implementar horario de profesores?
	pass

class Teacher(models.Model):
	"""Model definition for New."""

	first_name = models.CharField(max_length=250, verbose_name='Nombre')
	last_name = models.CharField(max_length=250, verbose_name='Apellido')
	# image
	email = models.EmailField(max_length=255, verbose_name="Email")
	active = models.BooleanField(default=True, verbose_name='Activo')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
	updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

	class Meta:
		verbose_name = "Profesor"
		verbose_name_plural = "Profesores"
		ordering = ['created', 'updated', ]
	
	def __str__(self):
		return ' '.join([self.first_name, self.last_name])