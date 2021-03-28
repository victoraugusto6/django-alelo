from django.forms import ModelForm

from alelo.base.models import Janeiro


class JaneiroValorNovoForm(ModelForm):
    class Meta:
        model = Janeiro
        fields = ['valor']
