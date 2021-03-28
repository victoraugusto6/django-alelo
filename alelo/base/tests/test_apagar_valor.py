import pytest
from django.urls import reverse

from alelo.base.models import Janeiro


@pytest.fixture
def valor(db):
    return Janeiro.objects.create(valor=20)


@pytest.fixture
def resposta(client, valor):
    resp = client.post(
        reverse('base:apagar', kwargs={'valor_id': valor.id})
    )
    return resp

# def test_apagar_valor(resposta):
#     assert not Janeiro.objects.exists()
