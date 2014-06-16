# -*- coding: utf-8 -*-
from django.utils import timezone

from modelos.ponto import Ponto, TipoPonto
from datetime import time, timedelta
from django.core.exceptions import ObjectDoesNotExist


def registrar_ponto(capacitando, user):
    pass


def controle_turno(turno, capacitando):
    dia_hora = timezone.localtime(timezone.now())

    ponto = Ponto()

    try:
        pontos = Ponto.objects.get(
            data=dia_hora.date(),
            capacitando=capacitando,
            tipo_ponto__id=1)

    except ObjectDoesNotExist:
        pontos = []

    if len(pontos) == 0:
        ponto.atraso = calculo_atraso(dia_hora, turno.entrada)
        ponto.tipo_ponto = TipoPonto.objects.get(pk=1)

    elif len(pontos) == 1:
        ponto.atraso = calculo_atraso(dia_hora, turno.saidaLanche)
        ponto.tipo_ponto = TipoPonto.objects.get(pk=2)
    elif len(pontos) == 2:
        ponto.atraso = calculo_atraso(dia_hora, turno.entradaLanche)
        ponto.tipo_ponto = TipoPonto.objects.get(pk=3)
    else:
        ponto.atraso = calculo_atraso(dia_hora, turno.saida)
        ponto.tipo_ponto = TipoPonto.objects.get(pk=4)

    ponto.data = dia_hora.date()
    ponto.hora = dia_hora.time()

    return ponto


def calculo_atraso(agora, horario):
    atraso = agora - \
        timedelta(hours=horario.hour,
                  minutes=horario.minute, seconds=horario.second)

    atraso = atraso.time()

    if atraso < time(0, 15):
        atraso = time(0, 0)

    return atraso
