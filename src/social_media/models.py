from django.db import models

# Create your models here.

class PostImage(models.Model):
	image = models.ImageField(verbose_name='Imágen', upload_to='posts_images')
	active = models.BooleanField(
		default=True, verbose_name='Activo', 
		help_text='Las filas con este campo desactivado no serán mostradas.'
	)
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

	class Meta:
		verbose_name = "Imagen de Post"
		verbose_name_plural = "Imágenes de Posts"

	def __str__(self):
		pass

class Post(models.Model):
	"""Model definition for Post."""

	# TODO: Define fields here
	text = models.TextField(blank=True, default='', verbose_name='Cuerpo/mensaje del post.')
	images = models.ForeignKey('PostImage', on_delete=models.CASCADE, null=True, verbose_name='Imágenes del post.')
	active = models.BooleanField(
		default=True, verbose_name='Activo', 
		help_text='Las filas con este campo desactivado no serán mostradas.'
	)
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

	class Meta:
		"""Meta definition for Post."""
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'

	def __str__(self):
		"""Unicode representation of Post."""
		return str(self.id)

	# TODO: Define custom methods here
