# -*- coding: utf-8 -*-
from django.utils import timezone

from modelos.ponto import Ponto, TipoPonto
from django.core.exceptions import ObjectDoesNotExist

PONTO_ENTRADA = 1
PONTO_SAIDA_LANCHE = 2
PONTO_ENTRADA_LANCHE = 3


def registrar_ponto(capacitando, user):
    tipo_ponto = obtem_tipo_ponto(capacitando)

    ponto = Ponto()
    ponto.capacitando = capacitando
    ponto.tipo_ponto = tipo_ponto
    ponto.user = user
    ponto.save()


def verifica_ponto(capacitando, ponto):
    dia_hora = timezone.localtime(timezone.now())
    try:
        ponto = Ponto.objects.get(
            data=dia_hora.date(),
            capacitando=capacitando,
            tipo_ponto__id=ponto)

        return True
    except ObjectDoesNotExist:
        return False


def obtem_tipo_ponto(capacitando):
    dia_hora = timezone.localtime(timezone.now())

    tipo_ponto = None

    if not verifica_ponto(capacitando, PONTO_ENTRADA):
        tipo_ponto = TipoPonto.objects.get(pk=1)
    else:
        if dia_hora.time() < capacitando.turno.entrada_lanche:
            tipo_ponto = TipoPonto.objects.get(pk=2)

        elif dia_hora.time() < capacitando.turno.saida:
            if not verifica_ponto(capacitando, PONTO_SAIDA_LANCHE):
                tipo_ponto = TipoPonto.objects.get(pk=4)

            elif verifica_ponto(capacitando, PONTO_ENTRADA_LANCHE):
                tipo_ponto = TipoPonto.objects.get(pk=4)
            else:
                tipo_ponto = TipoPonto.objects.get(pk=3)
        else:
            tipo_ponto = TipoPonto.objects.get(pk=4)

    return tipo_ponto
