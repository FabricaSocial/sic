from django.contrib import admin

# Register your models here.

from modelos.capacitando import Capacitando
from modelos.ponto import Ponto
from modelos.pessoa import Pessoa, Endereco, Naturalidade
from modelos.pessoa import CNH, CarteiraTrabalho, CategoriaCNH, Cidade

admin.site.register(Capacitando)
admin.site.register(Ponto)
admin.site.register(Pessoa)
admin.site.register(Endereco)
admin.site.register(Naturalidade)
admin.site.register(CNH)
admin.site.register(CarteiraTrabalho)
admin.site.register(CategoriaCNH)
admin.site.register(Cidade)
