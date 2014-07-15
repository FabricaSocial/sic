from django.contrib import admin

# Register your models here.

from modelos.pessoa import CategoriaCNH, Nacionalidade, TipoIdentidade, \
    TipoTelefone, Pais, Etnia, UF, Cidade, Naturalidade, Endereco, \
    EstadoCivil, Sexo, Pessoa, Reservista, RegistroGeral, ServicoMilitar, \
    CarteiraTrabalho, Filiacao, CNH, Telefone, Email, TituloEleitor
from modelos.capacitando import Categoria, NecessidadeEspecial, \
    Especialidade, AreaAtuacao, Turno, Capacitando, Desligamento
from modelos.funcionario import TipoAudit, Lotacao, Cargo, Funcionario, \
    FuncionarioAudit
from modelos.administrativo import Coordenadoria, CoordenadoriaAdjunta, \
    Ramal, Unidade, Departamento
from modelos.ponto import Ponto, TipoPonto

admin.site.register(CategoriaCNH)
admin.site.register(Nacionalidade)
admin.site.register(TipoIdentidade)
admin.site.register(TipoTelefone)
admin.site.register(Pais)
admin.site.register(Etnia)
admin.site.register(UF)
admin.site.register(Cidade)
admin.site.register(Naturalidade)
admin.site.register(Endereco)
admin.site.register(EstadoCivil)
admin.site.register(Sexo)
admin.site.register(Pessoa)
admin.site.register(Reservista)
admin.site.register(RegistroGeral)
admin.site.register(ServicoMilitar)
admin.site.register(CarteiraTrabalho)
admin.site.register(Filiacao)
admin.site.register(CNH)
admin.site.register(Telefone)
admin.site.register(Email)
admin.site.register(TituloEleitor)

admin.site.register(Categoria)
admin.site.register(NecessidadeEspecial)
admin.site.register(Especialidade)
admin.site.register(AreaAtuacao)
admin.site.register(Turno)
admin.site.register(Capacitando)
admin.site.register(Desligamento)

admin.site.register(TipoAudit)
admin.site.register(Lotacao)
admin.site.register(Cargo)
admin.site.register(Funcionario)
admin.site.register(FuncionarioAudit)

admin.site.register(Coordenadoria)
admin.site.register(CoordenadoriaAdjunta)
admin.site.register(Ramal)
admin.site.register(Unidade)
admin.site.register(Departamento)

admin.site.register(Ponto)
admin.site.register(TipoPonto)
