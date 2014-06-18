# -*- coding: utf-8 -*-
from django.utils import timezone

from modelos.ponto import Ponto, TipoPonto
from django.core.exceptions import ObjectDoesNotExist


def registrar_ponto(capacitando, user):
    #tipo_ponto = obtem_tipo_ponto(capacitando.turno)
    tipo_ponto = TipoPonto.objects.get(pk=1)

    ponto = Ponto()
    ponto.capacitando = capacitando
    ponto.tipo_ponto = tipo_ponto
    ponto.user = user
    ponto.save()


def verifica_ponto_entrada(capacitando):
    dia_hora = timezone.localtime(timezone.now())
    try:
        Ponto.objects.get(
            data=dia_hora.date(),
            capacitando=capacitando,
            tipo_ponto__id=1)

        return True
    except ObjectDoesNotExist:
        return False


def obtem_tipo_ponto(capacitando):
    dia_hora = timezone.localtime(timezone.now())

    tipo_ponto = None

    if not verifica_ponto_entrada(capacitando):
        tipo_ponto = TipoPonto.objects.get(pk=1)
    else:
        if dia_hora.time() < capacitando.turno.saida_lanche:
            tipo_ponto = TipoPonto.objects.get(pk=1)
        elif dia_hora.time() < capacitando.turno.entrada_lanche:
            tipo_ponto = TipoPonto.objects.get(pk=2)
        elif dia_hora.time() < capacitando.turno.saida:
            tipo_ponto = TipoPonto.objects.get(pk=3)
        else:
            tipo_ponto = TipoPonto.objects.get(pk=4)

    return tipo_ponto
