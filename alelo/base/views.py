from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from alelo.base.forms import JaneiroValorNovoForm, FevereiroValorNovoForm, MarcoValorNovoForm, AbrilValorNovoForm, \
    MaioValorNovoForm, JunhoValorNovoForm, JulhoValorNovoForm, AgostoValorNovoForm, SetembroValorNovoForm, \
    OutubroValorNovoForm, NovembroValorNovoForm, DezembroValorNovoForm
from alelo.base.models import Janeiro, Fevereiro, Marco, Abril, Maio, Junho, Julho, Agosto, Setembro, Outubro, Novembro, \
    Dezembro


def home(request):
    return render(request, 'base/home.html')


# Mês - Janeiro
@login_required
def janeiro(request):
    if request.method == 'POST':
        form = JaneiroValorNovoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('base:janeiro'))
        else:
            valores_mes = Janeiro.objects.all()
            return render(request, 'base/meses/janeiro.html', {'form': form, 'valores_mes': valores_mes}, status=400)

    total_mes_janeiro_dct = Janeiro.objects.aggregate(Sum('valor'))
    total_mes_janeiro = total_mes_janeiro_dct['valor__sum']
    valores_mes = Janeiro.objects.all()
    return render(request, 'base/meses/janeiro.html',
                  {'valores_mes': valores_mes, 'total_mes_janeiro': total_mes_janeiro})


def apagar_valor_janeiro(request, pk):
    valor = get_object_or_404(Janeiro, pk=pk)

    if request.method == 'POST':
        valor.delete()
        return HttpResponseRedirect(reverse('base:janeiro'))
    return render(request, 'base/meses/janeiro.html', {'valor': valor})


# Mês - Fevereiro
@login_required
def fevereiro(request):
    if request.method == 'POST':
        form = FevereiroValorNovoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('base:fevereiro'))
        else:
            valores_mes = Fevereiro.objects.all()
            return render(request, 'base/meses/fevereiro.html', {'form': form, 'valores_mes': valores_mes}, status=400)

    total_mes_fevereiro_dct = Fevereiro.objects.aggregate(Sum('valor'))
    total_mes_fevereiro = total_mes_fevereiro_dct['valor__sum']
    valores_mes = Fevereiro.objects.all()
    return render(request, 'base/meses/fevereiro.html',
                  {'valores_mes': valores_mes, 'total_mes_fevereiro': total_mes_fevereiro})


def apagar_valor_fevereiro(request, pk):
    valor = get_object_or_404(Fevereiro, pk=pk)

    if request.method == 'POST':
        valor.delete()
        return HttpResponseRedirect(reverse('base:fevereiro'))
    return render(request, 'base/meses/fevereiro.html', {'valor': valor})


# Mês - Março
@login_required
def marco(request):
    if request.method == 'POST':
        form = MarcoValorNovoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('base:marco'))
        else:
            valores_mes = Marco.objects.all()
            return render(request, 'base/meses/marco.html', {'form': form, 'valores_mes': valores_mes}, status=400)

    total_mes_marco_dct = Marco.objects.aggregate(Sum('valor'))
    total_mes_marco = total_mes_marco_dct['valor__sum']
    valores_mes = Marco.objects.all()
    return render(request, 'base/meses/marco.html', {'valores_mes': valores_mes, 'total_mes_marco': total_mes_marco})


def apagar_valor_marco(request, pk):
    valor = get_object_or_404(Marco, pk=pk)

    if request.method == 'POST':
        valor.delete()
        return HttpResponseRedirect(reverse('base:marco'))
    return render(request, 'base/meses/marco.html', {'valor': valor})


# Mês - Abril
@login_required
def abril(request):
    if request.method == 'POST':
        form = AbrilValorNovoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('base:abril'))
        else:
            valores_mes = Abril.objects.all()
            return render(request, 'base/meses/abril.html', {'form': form, 'valores_mes': valores_mes}, status=400)

    total_mes_abril_dct = Abril.objects.aggregate(Sum('valor'))
    total_mes_abril = total_mes_abril_dct['valor__sum']
    valores_mes = Abril.objects.all()
    return render(request, 'base/meses/abril.html', {'valores_mes': valores_mes, 'total_mes_abril': total_mes_abril})


def apagar_valor_abril(request, pk):
    valor = get_object_or_404(Abril, pk=pk)

    if request.method == 'POST':
        valor.delete()
        return HttpResponseRedirect(reverse('base:abril'))
    return render(request, 'base/meses/abril.html', {'valor': valor})


# Mês - Maio
@login_required
def maio(request):
    if request.method == 'POST':
        form = MaioValorNovoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('base:maio'))
        else:
            valores_mes = Maio.objects.all()
            return render(request, 'base/meses/maio.html', {'form': form, 'valores_mes': valores_mes}, status=400)

    total_mes_maio_dct = Maio.objects.aggregate(Sum('valor'))
    total_mes_maio = total_mes_maio_dct['valor__sum']
    valores_mes = Maio.objects.all()
    return render(request, 'base/meses/maio.html', {'valores_mes': valores_mes, 'total_mes_maio': total_mes_maio})


def apagar_valor_maio(request, pk):
    valor = get_object_or_404(Maio, pk=pk)

    if request.method == 'POST':
        valor.delete()
        return HttpResponseRedirect(reverse('base:maio'))
    return render(request, 'base/meses/maio.html', {'valor': valor})


# Mês - Junho
@login_required
def junho(request):
    if request.method == 'POST':
        form = JunhoValorNovoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('base:junho'))
        else:
            valores_mes = Junho.objects.all()
            return render(request, 'base/meses/junho.html', {'form': form, 'valores_mes': valores_mes}, status=400)

    total_mes_junho_dct = Junho.objects.aggregate(Sum('valor'))
    total_mes_junho = total_mes_junho_dct['valor__sum']
    valores_mes = Junho.objects.all()
    return render(request, 'base/meses/junho.html', {'valores_mes': valores_mes, 'total_mes_junho': total_mes_junho})


def apagar_valor_junho(request, pk):
    valor = get_object_or_404(Junho, pk=pk)

    if request.method == 'POST':
        valor.delete()
        return HttpResponseRedirect(reverse('base:junho'))
    return render(request, 'base/meses/junho.html', {'valor': valor})


# Mês - Julho
@login_required
def julho(request):
    if request.method == 'POST':
        form = JulhoValorNovoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('base:julho'))
        else:
            valores_mes = Julho.objects.all()
            return render(request, 'base/meses/julho.html', {'form': form, 'valores_mes': valores_mes}, status=400)

    total_mes_julho_dct = Julho.objects.aggregate(Sum('valor'))
    total_mes_julho = total_mes_julho_dct['valor__sum']
    valores_mes = Julho.objects.all()
    return render(request, 'base/meses/julho.html', {'valores_mes': valores_mes, 'total_mes_julho': total_mes_julho})


def apagar_valor_julho(request, pk):
    valor = get_object_or_404(Julho, pk=pk)

    if request.method == 'POST':
        valor.delete()
        return HttpResponseRedirect(reverse('base:julho'))
    return render(request, 'base/meses/julho.html', {'valor': valor})


# Mês - Agosto
@login_required
def agosto(request):
    if request.method == 'POST':
        form = AgostoValorNovoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('base:agosto'))
        else:
            valores_mes = Agosto.objects.all()
            return render(request, 'base/meses/agosto.html', {'form': form, 'valores_mes': valores_mes}, status=400)

    total_mes_agosto_dct = Agosto.objects.aggregate(Sum('valor'))
    total_mes_agosto = total_mes_agosto_dct['valor__sum']
    valores_mes = Agosto.objects.all()
    return render(request, 'base/meses/agosto.html', {'valores_mes': valores_mes, 'total_mes_agosto': total_mes_agosto})


def apagar_valor_agosto(request, pk):
    valor = get_object_or_404(Agosto, pk=pk)

    if request.method == 'POST':
        valor.delete()
        return HttpResponseRedirect(reverse('base:agosto'))
    return render(request, 'base/meses/agosto.html', {'valor': valor})


# Mês - Setembro
@login_required
def setembro(request):
    if request.method == 'POST':
        form = SetembroValorNovoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('base:setembro'))
        else:
            valores_mes = Setembro.objects.all()
            return render(request, 'base/meses/setembro.html', {'form': form, 'valores_mes': valores_mes}, status=400)

    total_mes_setembro_dct = Setembro.objects.aggregate(Sum('valor'))
    total_mes_setembro = total_mes_setembro_dct['valor__sum']
    valores_mes = Setembro.objects.all()
    return render(request, 'base/meses/setembro.html',
                  {'valores_mes': valores_mes, 'total_mes_setembro': total_mes_setembro})


def apagar_valor_setembro(request, pk):
    valor = get_object_or_404(Setembro, pk=pk)

    if request.method == 'POST':
        valor.delete()
        return HttpResponseRedirect(reverse('base:setembro'))
    return render(request, 'base/meses/setembro.html', {'valor': valor})


# Mês - Outubro
@login_required
def outubro(request):
    if request.method == 'POST':
        form = OutubroValorNovoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('base:outubro'))
        else:
            valores_mes = Outubro.objects.all()
            return render(request, 'base/meses/outubro.html', {'form': form, 'valores_mes': valores_mes}, status=400)

    total_mes_outubro_dct = Outubro.objects.aggregate(Sum('valor'))
    total_mes_outubro = total_mes_outubro_dct['valor__sum']
    valores_mes = Outubro.objects.all()
    return render(request, 'base/meses/outubro.html',
                  {'valores_mes': valores_mes, 'total_mes_outubro': total_mes_outubro})


def apagar_valor_outubro(request, pk):
    valor = get_object_or_404(Outubro, pk=pk)

    if request.method == 'POST':
        valor.delete()
        return HttpResponseRedirect(reverse('base:outubro'))
    return render(request, 'base/meses/outubro.html', {'valor': valor})


# Mês - Novembro
@login_required
def novembro(request):
    if request.method == 'POST':
        form = NovembroValorNovoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('base:novembro'))
        else:
            valores_mes = Novembro.objects.all()
            return render(request, 'base/meses/novembro.html', {'form': form, 'valores_mes': valores_mes}, status=400)

    total_mes_novembro_dct = Novembro.objects.aggregate(Sum('valor'))
    total_mes_novembro = total_mes_novembro_dct['valor__sum']
    valores_mes = Novembro.objects.all()
    return render(request, 'base/meses/novembro.html',
                  {'valores_mes': valores_mes, 'total_mes_novembro': total_mes_novembro})


def apagar_valor_novembro(request, pk):
    valor = get_object_or_404(Novembro, pk=pk)

    if request.method == 'POST':
        valor.delete()
        return HttpResponseRedirect(reverse('base:novembro'))
    return render(request, 'base/meses/novembro.html', {'valor': valor})


# Mês - Dezembro
@login_required
def dezembro(request):
    if request.method == 'POST':
        form = DezembroValorNovoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('base:dezembro'))
        else:
            valores_mes = Dezembro.objects.all()
            return render(request, 'base/meses/dezembro.html', {'form': form, 'valores_mes': valores_mes}, status=400)

    total_mes_dezembro_dct = Dezembro.objects.aggregate(Sum('valor'))
    total_mes_dezembro = total_mes_dezembro_dct['valor__sum']
    valores_mes = Dezembro.objects.all()
    return render(request, 'base/meses/dezembro.html',
                  {'valores_mes': valores_mes, 'total_mes_dezembro': total_mes_dezembro})


def apagar_valor_dezembro(request, pk):
    valor = get_object_or_404(Dezembro, pk=pk)

    if request.method == 'POST':
        valor.delete()
        return HttpResponseRedirect(reverse('base:dezembro'))
    return render(request, 'base/meses/dezembro.html', {'valor': valor})
