from django.db import models


class Fichero(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=240)
	fichero = models.FileField(upload_to='files')

	def __str__(self):
		return self.name