from django.db import models

from access_db import models as access_db


class TipoEntrada(models.Model):

    class Meta:
        verbose_name = ('TipoEntrada')
        verbose_name_plural = ('TipoEntradas')

    def __unicode__(self):
        pass

    descricao = models.CharField(max_length=50)


class Ponto(models.Model):

    class Meta:
        verbose_name = ('Ponto')
        verbose_name_plural = ('Pontos')

    def __unicode__(self):
        pass

    capacitando = models.ForeignKey(access_db.Tbassiduidade)
    dia = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    tipo_entrada = models.ForeignKey('TipoEntrada')
