from django.forms import ModelForm
from .models import Fichero


class FicheroForm(ModelForm):
	class Meta:
		model = Fichero
		exclude= ("created_at","name")