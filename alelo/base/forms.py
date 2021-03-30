from django.forms import ModelForm

from alelo.base.models import Janeiro, Dezembro, Novembro, Outubro, Setembro, Agosto, Julho, Junho, Maio, Abril, Marco, \
    Fevereiro


class JaneiroValorNovoForm(ModelForm):
    class Meta:
        model = Janeiro
        fields = ['valor']


class FevereiroValorNovoForm(ModelForm):
    class Meta:
        model = Fevereiro
        fields = ['valor']


class MarcoValorNovoForm(ModelForm):
    class Meta:
        model = Marco
        fields = ['valor']


class AbrilValorNovoForm(ModelForm):
    class Meta:
        model = Abril
        fields = ['valor']


class MaioValorNovoForm(ModelForm):
    class Meta:
        model = Maio
        fields = ['valor']


class JunhoValorNovoForm(ModelForm):
    class Meta:
        model = Junho
        fields = ['valor']


class JulhoValorNovoForm(ModelForm):
    class Meta:
        model = Julho
        fields = ['valor']


class AgostoValorNovoForm(ModelForm):
    class Meta:
        model = Agosto
        fields = ['valor']


class SetembroValorNovoForm(ModelForm):
    class Meta:
        model = Setembro
        fields = ['valor']


class OutubroValorNovoForm(ModelForm):
    class Meta:
        model = Outubro
        fields = ['valor']


class NovembroValorNovoForm(ModelForm):
    class Meta:
        model = Novembro
        fields = ['valor']


class DezembroValorNovoForm(ModelForm):
    class Meta:
        model = Dezembro
        fields = ['valor']
