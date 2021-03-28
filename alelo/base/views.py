from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from alelo.base.forms import JaneiroValorNovoForm
from alelo.base.models import Janeiro


def home(request):
    return render(request, 'base/home.html')


def meses(request):
    if request.method == 'POST':
        form = JaneiroValorNovoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('base:meses'))
        else:
            valores_mes = Janeiro.objects.all()
            return render(request, 'base/meses.html', {'form': form, 'valores_mes': valores_mes}, status=400)

    valores_mes = Janeiro.objects.all()
    return render(request, 'base/meses.html', {'valores_mes': valores_mes})


def apagar(request, tarefa_id):
    if request.method == 'POST':
        Janeiro.objects.filter(id=tarefa_id).delete()
    return HttpResponseRedirect('base:meses')
