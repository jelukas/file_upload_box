from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import simplejson
from .models import Fichero
from .forms import FicheroForm

class JsonResponse(HttpResponse):
	def __init__(self,data,**kwargs):
		HttpResponse.__init__(self,content=simplejson.dumps(data),mimetype='application/json',**kwargs)

def home(request):
	context = {}
	upload_form = FicheroForm()
	context.update({'upload_form': upload_form})
	return render_to_response('boxes/home.html',context,context_instance=RequestContext(request))


def upload_file(request):
	if request.POST:
		status = 400
		response = None
		upload_form = FicheroForm(request.POST,request.FILES)
		if upload_form.is_valid():
			fichero = upload_form.save(commit=False)
			fichero.name = fichero.fichero.name
			fichero.save()
			status = 200
			response = {'success': 200}
		else:
			status = 400
			response = {'error': 400}
			response.update({'errors': upload_form.errors })
		return JsonResponse(response,status=status)