from django import models

class CategoriaCNH(models.Model):
  categoria = models.CharField(max_length=45)
  class Meta:
    db_table = 'CategoriaCNH'

class Nacionalidade(models.Model):
  descricao = models.CharField(max_length=255)
  class Meta:
    db_table = 'Nacionalidade'

class TipoIdentidade(models.Model):
  descricao = models.CharField(max_length=255)
  class Meta:
    db_table = 'TipoIdentidade'

