import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

from alelo.base.models import Janeiro


@pytest.fixture
def resposta(client, db):
    resp = client.get(reverse('base:meses'))
    return resp


def test_status_code(resposta):
    assert resposta.status_code == 200


def test_formulario_presente(resposta):
    assertContains(resposta, '<form')


def test_botao_tipo_submit(resposta):
    assertContains(resposta, ' <button type="submit"')


@pytest.fixture
def lista_de_valores(db):
    valores = [
        Janeiro(valor=20),
        Janeiro(valor=40),
    ]
    Janeiro.objects.bulk_create(valores)
    return valores


@pytest.fixture
def resposta_com_lista_de_valores(client, lista_de_valores):
    resp = client.get(reverse('base:meses'))
    return resp


def test_lista_de_valores_presente(resposta_com_lista_de_valores, lista_de_valores):
    for valor in lista_de_valores:
        assertContains(resposta_com_lista_de_valores, valor.valor)
