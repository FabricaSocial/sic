# -*- coding: utf-8 -*-

from modelos.models import Ponto, TipoEntrada
from datetime import datetime, time


def obter_tipo_entrada():
    dia_hora = datetime.now()
    hora = dia_hora.time()

    if hora < time(13, 30):
        tipo_entrada_id = entrada_matutino(hora)
    else:
        tipo_entrada_id = entrada_vespertino(hora)

    print tipo_entrada_id
    tipo_entrada = TipoEntrada.objects.get(pk=tipo_entrada_id)


def entrada_matutino(hora):
    if hora >= time(7, 50) and hora < time(8, 30):
        tipo_entrada = 1
    elif hora >= time(9, 30) and hora < time(10, 10):
        tipo_entrada = 2
    elif hora >= time(10, 10) and hora < time(10, 50):
        tipo_entrada = 3
    elif hora >= time(11, 30) and hora < time(12, 30):
        tipo_entrada = 4
    else:
        tipo_entrada = 5

    return tipo_entrada


def entrada_vespertino(hora):
    if hora >= time(13, 50) and hora < time(14, 30):
        tipo_entrada = 1
    elif hora >= time(15, 30) and hora < time(16, 10):
        tipo_entrada = 2
    elif hora >= time(16, 10) and hora < time(16, 50):
        tipo_entrada = 3
    elif hora >= time(17, 30) and hora < time(18, 30):
        tipo_entrada = 4
    else:
        tipo_entrada = 5

    return tipo_entrada
