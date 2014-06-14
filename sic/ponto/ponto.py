# -*- coding: utf-8 -*-

from modelos.models import Ponto, Turno
from datetime import datetime, time


def obter_turno(capacitando):
    dia_hora = datetime.now()
    hora = dia_hora.time()

    if hora < time(13, 30):
        turno_id = entrada_matutino(hora)
    else:
        turno_id = entrada_vespertino(hora)

    print turno_id
    turno = Turno.objects.get(pk=turno_id)


def entrada_matutino(hora):
    if hora >= time(7, 50) and hora < time(8, 30):
        turno = 1
    elif hora >= time(9, 30) and hora < time(10, 10):
        turno = 2
    elif hora >= time(10, 10) and hora < time(10, 50):
        turno = 3
    elif hora >= time(11, 30) and hora < time(12, 30):
        turno = 4
    else:
        turno = 5

    return turno


def entrada_vespertino(hora):
    if hora >= time(13, 50) and hora < time(14, 30):
        turno = 1
    elif hora >= time(15, 30) and hora < time(16, 10):
        turno = 2
    elif hora >= time(16, 10) and hora < time(16, 50):
        turno = 3
    elif hora >= time(17, 30) and hora < time(18, 30):
        turno = 4
    else:
        turno = 5

    return turno
