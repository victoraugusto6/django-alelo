import pytest
from django.urls import reverse
from alelo.base.models import Janeiro


@pytest.fixture
def resposta(client, db):
    resp = client.post(reverse('base:meses'), data={'valor': 20.00})
    return resp


@pytest.fixture
def resposta_dado_invalido(client, db):
    resp = client.post(reverse('base:meses'), data={'valor': ''})
    return resp


def test_valor_existe_no_bd(resposta):
    assert Janeiro.objects.exists()


def test_redirecionamento_depois_do_salvamento(resposta):
    assert resposta.status_code == 302


def test_valor_nao_existe_no_bd(resposta_dado_invalido):
    assert not Janeiro.objects.exists()


def test_pagina_com_dados_invalidos(resposta_dado_invalido):
    assert resposta_dado_invalido.status_code == 400
