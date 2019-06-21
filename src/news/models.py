from django.db import models

# Create your models here.
class New(models.Model):
	"""Model definition for New."""

	title = models.CharField(max_length=250, verbose_name='Título')
	body = models.TextField(verbose_name='Cuerpo de la noticia', blank=False, null=False)
	# author = models.CharField(max_length=50) # definir con user
	active = models.BooleanField(default=True, verbose_name='Activo')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
	updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

	class Meta:
		verbose_name = "Noticia"
		verbose_name_plural = "Noticias"
		ordering = ['created', 'updated', ]
	
	def __str__(self):
		return self.tittle