from django.db import models

# Create your models here.
class Material(models.Model):
	semester = models.PositiveIntegerField(blank=False, null=False, verbose_name="Semestre")
	subject = models.CharField(max_length=150, blank=False, null=False, verbose_name="Asignatura")
	ffile = models.FileField(null=False, verbose_name="Archivo")
	active = models.BooleanField(default=True, verbose_name='Activo')
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

	class Meta:
		"""Meta definition for Material."""
		verbose_name = 'Material de Apoyo'
		verbose_name_plural = 'Materiales de Apoyo'

	def __str__(self):
		return self.ffile.name
