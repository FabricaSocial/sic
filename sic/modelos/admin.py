from django.contrib import admin

# Register your models here.

from modelos.capacitando import Capacitando
from modelos.ponto import Ponto
from modelos.pessoa import Pessoa, Endereco, Naturalidade
from modelos.pessoa import CNH, CarteiraTrabalho, CategoriaCNH, Cidade
from modelos.administrativo import Coordenadoria, CoordenadoriaAdjunta
from modelos.administrativo import Departamento, Ramal, Unidade
from modelos.funcionario import Cargo, Funcionario, Lotacao

admin.site.register(Capacitando)
admin.site.register(Ponto)
admin.site.register(Pessoa)
admin.site.register(Endereco)
admin.site.register(Naturalidade)
admin.site.register(CNH)
admin.site.register(CarteiraTrabalho)
admin.site.register(CategoriaCNH)
admin.site.register(Cidade)
admin.site.register(Coordenadoria)
admin.site.register(CoordenadoriaAdjunta)
admin.site.register(Departamento)
admin.site.register(Ramal)
admin.site.register(Unidade)
admin.site.register(Cargo)
admin.site.register(Funcionario)
admin.site.register(Lotacao)
