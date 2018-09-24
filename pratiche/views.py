from django.shortcuts import render
from .models import Pratica, Agente

def pratica_list_view(request):
	if request.method == 'POST':
		agente = request.POST.get('cboAgent')
		if agente == 'all':
			object_list = Pratica.objects.all()
		else:
			object_list = Pratica.objects.filter(agente = agente)
	else:
		object_list = Pratica.objects.all()

	agenti_list = Agente.objects.all()
	context = {
		'object_list': object_list,
		'agenti_list': agenti_list,
	}
	return render(request, 'pratiche/pratica_list.html', context)


def pratica_detail_view(request, id=id):
	obj = Pratica.objects.get(id=id)
	context = {
		'object': obj
	}
	return render(request, 'pratiche/pratica_detail.html', context)
# Create your views here.
