# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Anos(models.Model):
    # Field name made lowercase.
    ano = models.IntegerField(db_column='Ano', primary_key=True)

    class Meta:
        managed = False
        db_table = 'Anos'


class Meses(models.Model):
    # Field name made lowercase.
    codmes = models.IntegerField(db_column='CodMes', primary_key=True)
    # Field name made lowercase.
    mes = models.CharField(db_column='Mes', max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'Meses'


class Tbativos(models.Model):
    cdativo = models.IntegerField(primary_key=True)
    matricula = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'TBAtivos'


class Tabescolaridade(models.Model):
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    c_digo = models.IntegerField(db_column='C\xf3digo', primary_key=True)
    # Field name made lowercase.
    escolaridade = models.CharField(
        db_column='Escolaridade', max_length=50, blank=True)
    # Field name made lowercase.
    areaformacao = models.CharField(
        db_column='AreaFormacao', max_length=50, blank=True)
    # Field name made lowercase.
    faculdade = models.IntegerField(
        db_column='Faculdade', blank=True, null=True)
    # Field name made lowercase.
    curso = models.CharField(db_column='Curso', max_length=255, blank=True)
    # Field name made lowercase.
    turnofac = models.CharField(
        db_column='TurnoFac', max_length=50, blank=True)
    hore = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=11)
    anoconclusao = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    atual = models.IntegerField(db_column='Atual', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TabEscolaridade'


class Tabescolas(models.Model):
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    c_digo = models.IntegerField(db_column='C\xf3digo', primary_key=True)
    # Field name made lowercase.
    escola = models.CharField(db_column='Escola', max_length=255, blank=True)
    # Field name made lowercase.
    cnpj = models.FloatField(db_column='CNPJ', blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True)
    municipio = models.CharField(max_length=255, blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    cep = models.CharField(max_length=8, blank=True)
    # Field name made lowercase.
    tcomercial = models.CharField(
        db_column='Tcomercial', max_length=10, blank=True)
    # Field name made lowercase.
    tfax = models.CharField(db_column='TFax', max_length=10, blank=True)
    # Field name made lowercase.
    tcelular = models.CharField(
        db_column='TCelular', max_length=10, blank=True)
    email = models.CharField(max_length=255, blank=True)
    # Field name made lowercase.
    responsavel = models.CharField(
        db_column='Responsavel', max_length=255, blank=True)
    # Field name made lowercase.
    qalunos = models.IntegerField(db_column='Qalunos', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_6 = models.IntegerField(db_column='6', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_8 = models.IntegerField(db_column='8', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_10 = models.IntegerField(db_column='10', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_12 = models.IntegerField(db_column='12', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_14 = models.IntegerField(db_column='14', blank=True, null=True)
    # Field name made lowercase.
    pp = models.IntegerField(db_column='PP', blank=True, null=True)
    # Field name made lowercase.
    p = models.IntegerField(db_column='P', blank=True, null=True)
    # Field name made lowercase.
    m = models.IntegerField(db_column='M', blank=True, null=True)
    # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)
    # Field name made lowercase.
    gg = models.IntegerField(db_column='GG', blank=True, null=True)
    # Field name made lowercase.
    ppa = models.IntegerField(db_column='PPA', blank=True, null=True)
    # Field name made lowercase.
    pa = models.IntegerField(db_column='PA', blank=True, null=True)
    # Field name made lowercase.
    ma = models.IntegerField(db_column='MA', blank=True, null=True)
    # Field name made lowercase.
    ga = models.IntegerField(db_column='GA', blank=True, null=True)
    # Field name made lowercase.
    gga = models.IntegerField(db_column='GGA', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TabEscolas'


class Tabferiados(models.Model):
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    c_digo = models.IntegerField(db_column='C\xf3digo', primary_key=True)
    data = models.DateTimeField(blank=True, null=True)
    acontecimento = models.CharField(max_length=255, blank=True)
    descricao = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'TabFeriados'


class Tabfuncional(models.Model):
    codfuncional = models.IntegerField(primary_key=True)
    # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', unique=True, max_length=11)
    # Field name made lowercase.
    matricula = models.CharField(
        db_column='Matricula', max_length=50, blank=True)
    # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True)
    # Field name made lowercase.
    cargo = models.CharField(db_column='Cargo', max_length=255, blank=True)
    dtnomeacao = models.DateTimeField(blank=True, null=True)
    # Field name made lowercase.
    dtposse = models.DateTimeField(db_column='Dtposse', blank=True, null=True)
    dtexercicio = models.DateTimeField(blank=True, null=True)
    # Field name made lowercase.
    turno = models.CharField(db_column='Turno', max_length=50, blank=True)
    # Field name made lowercase.
    escala = models.CharField(db_column='Escala', max_length=255, blank=True)
    # Field name made lowercase.
    cargahoraria = models.CharField(
        db_column='CargaHoraria', max_length=50, blank=True)
    # Field name made lowercase.
    horario = models.CharField(db_column='Horario', max_length=50, blank=True)
    # Field name made lowercase.
    telefonelot = models.CharField(
        db_column='TelefoneLot', max_length=255, blank=True)
    # Field name made lowercase.
    datadeslig = models.DateTimeField(
        db_column='DataDeslig', blank=True, null=True)
    # Field name made lowercase.
    servidordeslig = models.IntegerField(
        db_column='ServidorDeslig', blank=True, null=True)
    # Field name made lowercase.
    classe = models.CharField(db_column='Classe', max_length=50, blank=True)
    # Field name made lowercase.
    padrao = models.CharField(db_column='Padrao', max_length=50, blank=True)
    # Field name made lowercase.
    trabalhasabado = models.IntegerField(
        db_column='TrabalhaSabado', blank=True, null=True)
    # Field name made lowercase.
    quinzenalmente = models.IntegerField(
        db_column='Quinzenalmente', blank=True, null=True)
    # Field name made lowercase.
    cargoefetivo = models.CharField(
        db_column='CargoEfetivo', max_length=50, blank=True)
    # Field name made lowercase.
    celetista = models.IntegerField(
        db_column='Celetista', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    situa_ofuncional = models.CharField(
        db_column='Situa\xe7\xe3oFuncional', max_length=150, blank=True)
    # Field name made lowercase.
    funcao = models.CharField(db_column='Funcao', max_length=50, blank=True)
    # Field name made lowercase.
    codlotacao = models.CharField(
        db_column='CodLotacao', max_length=50, blank=True)
    # Field name made lowercase.
    desclotacao = models.CharField(
        db_column='DescLotacao', max_length=255, blank=True)
    # Field name made lowercase.
    codorgaoorigem = models.IntegerField(
        db_column='CodOrgaoOrigem', blank=True, null=True)
    # Field name made lowercase.
    descoo = models.CharField(db_column='DescOO', max_length=255, blank=True)
    # Field name made lowercase.
    cargooo = models.CharField(db_column='CargoOO', max_length=255, blank=True)
    # Field name made lowercase.
    rnatal = models.IntegerField(db_column='RNatal', blank=True, null=True)
    # Field name made lowercase.
    ranovo = models.IntegerField(db_column='RANovo', blank=True, null=True)
    # Field name made lowercase.
    especialidade = models.CharField(
        db_column='Especialidade', max_length=255, blank=True)
    # Field name made lowercase.
    obs = models.TextField(db_column='Obs', blank=True)
    sigla = models.CharField(max_length=255, blank=True)
    # Field name made lowercase.
    matroorigem = models.CharField(
        db_column='MatrOOrigem', max_length=255, blank=True)
    dtinclusao = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'TabFuncional'


class Tabfuncionarios(models.Model):
    codcpf = models.IntegerField(db_column='CodCPF', primary_key=True)
    cpf = models.CharField(db_column='CPF', unique=True, max_length=11)
    nome = models.CharField(db_column='Nome', max_length=255, blank=True)
    nomepai = models.CharField(db_column='NomePai', max_length=255, blank=True)
    nomemae = models.CharField(db_column='NomeMae', max_length=255, blank=True)
    sexo = models.CharField(db_column='Sexo', max_length=50, blank=True)
    estadocivil = models.CharField(
        db_column='EstadoCivil', max_length=50, blank=True)
    datanascimento = models.DateTimeField(
        db_column='DataNascimento', blank=True, null=True)
    cartestrangeiro = models.CharField(
        db_column='CartEstrangeiro', max_length=255, blank=True)
    pispasep = models.FloatField(db_column='PISPasep', blank=True, null=True)
    dtpis = models.DateTimeField(db_column='DtPis', blank=True, null=True)
    rg = models.CharField(db_column='RG', max_length=50, blank=True)
    orgaoexpedidor = models.CharField(
        db_column='OrgaoExpedidor', max_length=50, blank=True)
    ufexp = models.CharField(db_column='UFexp', max_length=2, blank=True)
    dataexp = models.DateTimeField(db_column='DataExp', blank=True, null=True)
    tituloeleitor = models.FloatField(
        db_column='TituloEleitor', blank=True, null=True)
    zonat = models.IntegerField(db_column='Zonat', blank=True, null=True)
    se_ot = models.IntegerField(
        db_column='Se\xe7\xe3ot', blank=True, null=True)
    municipiot = models.CharField(
        db_column='Municipiot', max_length=255, blank=True)
    uft = models.CharField(db_column='UFt', max_length=255, blank=True)
    endereco = models.CharField(
        db_column='Endereco', max_length=255, blank=True)
    cidade = models.CharField(db_column='Cidade', max_length=50, blank=True)
    estado = models.CharField(db_column='Estado', max_length=2, blank=True)
    bairro = models.CharField(db_column='Bairro', max_length=50, blank=True)
    cep = models.FloatField(db_column='CEP', blank=True, null=True)
    telefoneres = models.FloatField(
        db_column='TelefoneRes', blank=True, null=True)
    telefonecelular = models.FloatField(
        db_column='TelefoneCelular', blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=255, blank=True)
    filhos = models.IntegerField(db_column='Filhos', blank=True, null=True)
    pne = models.IntegerField(db_column='PNE', blank=True, null=True)
    qualdef = models.CharField(db_column='QualDef', max_length=255, blank=True)
    nac = models.CharField(db_column='Nac', max_length=255, blank=True)
    paisorigem = models.CharField(
        db_column='PaisOrigem', max_length=255, blank=True)
    nat = models.CharField(db_column='Nat', max_length=255, blank=True)
    uf = models.CharField(db_column='UF', max_length=2, blank=True)
    ra_a = models.CharField(db_column='Ra\xe7a', max_length=765, blank=True)
    cnh = models.FloatField(db_column='CNH', blank=True, null=True)
    ufcnh = models.CharField(db_column='UFcnh', max_length=2, blank=True)
    categoria = models.CharField(
        db_column='Categoria', max_length=3, blank=True)
    datacnh = models.DateTimeField(blank=True, null=True)
    validadecnh = models.DateTimeField(blank=True, null=True)
    creserva = models.FloatField(db_column='Creserva', blank=True, null=True)
    seriecr = models.IntegerField(db_column='SerieCR', blank=True, null=True)
    orgaocr = models.CharField(max_length=2, blank=True)
    categoriacr = models.CharField(
        db_column='CategoriaCR', max_length=255, blank=True)
    anoservico = models.IntegerField(
        db_column='AnoServico', blank=True, null=True)
    cdi = models.IntegerField(db_column='CDI', blank=True, null=True)
    umilitar = models.CharField(db_column='UMilitar', max_length=8, blank=True)
    ufservico = models.CharField(
        db_column='UFservico', max_length=2, blank=True)
    conjuge = models.CharField(max_length=255, blank=True)
    localfoto = models.CharField(
        db_column='LocalFoto', max_length=255, blank=True)
    area = models.CharField(max_length=255, blank=True)
    subarea = models.CharField(max_length=255, blank=True)
    status = models.CharField(db_column='Status', max_length=255, blank=True)
    datadesliga = models.DateTimeField(
        db_column='Datadesliga', blank=True, null=True)
    unidade = models.CharField(db_column='Unidade', max_length=255, blank=True)
    dtinclusao = models.DateTimeField(blank=True, null=True)
    nis = models.FloatField(db_column='NIS', blank=True, null=True)
    usuario = models.CharField(max_length=255, blank=True)
    datareg = models.DateTimeField(blank=True, null=True)
    responsavel = models.IntegerField(blank=True, null=True)
    ctps = models.FloatField(db_column='CTPS', blank=True, null=True)
    s_riectps = models.IntegerField(
        db_column='S\xe9rieCTPS', blank=True, null=True)
    rc = models.DecimalField(
        db_column='RC', max_digits=19, decimal_places=4, blank=True, null=True)
    acl = models.IntegerField(db_column='ACL', blank=True, null=True)
    pcd = models.IntegerField(db_column='PCD', blank=True, null=True)
    pi = models.IntegerField(db_column='PI', blank=True, null=True)
    cg = models.IntegerField(db_column='CG', blank=True, null=True)
    turno = models.CharField(max_length=255, blank=True)
    cdfamilia = models.FloatField(blank=True, null=True)
    matricula = models.IntegerField(blank=True, null=True)
    horareg = models.DateTimeField(blank=True, null=True)
    limiteat = models.DateTimeField(blank=True, null=True)
    diativ = models.DateTimeField(db_column='DIAtiv', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TabFuncionarios'


class Tabginasios(models.Model):
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    c_digo = models.IntegerField(db_column='C\xf3digo', primary_key=True)
    # Field name made lowercase.
    fantasia = models.CharField(
        db_column='Fantasia', max_length=255, blank=True)
    # Field name made lowercase.
    razao = models.CharField(db_column='Razao', max_length=255, blank=True)
    # Field name made lowercase.
    cnpj = models.FloatField(db_column='CNPJ', blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True)
    municipio = models.CharField(max_length=255, blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    cep = models.FloatField(blank=True, null=True)
    # Field name made lowercase.
    tcomercial = models.FloatField(
        db_column='Tcomercial', blank=True, null=True)
    # Field name made lowercase.
    tfax = models.FloatField(db_column='TFax', blank=True, null=True)
    # Field name made lowercase.
    tcelular = models.FloatField(db_column='TCelular', blank=True, null=True)
    # Field name made lowercase.
    responsavel = models.CharField(
        db_column='Responsavel', max_length=255, blank=True)
    # Field name made lowercase.
    qf = models.IntegerField(db_column='QF', blank=True, null=True)
    # Field name made lowercase.
    qm = models.IntegerField(db_column='QM', blank=True, null=True)
    # Field name made lowercase.
    cc = models.FloatField(db_column='CC', blank=True, null=True)
    # Field name made lowercase.
    banco = models.FloatField(db_column='Banco', blank=True, null=True)
    # Field name made lowercase.
    agencia = models.FloatField(db_column='Agencia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TabGinasios'


class Tabinsumo(models.Model):
    cd_insumo = models.IntegerField(primary_key=True)
    insumo = models.CharField(max_length=255, blank=True)
    medida = models.CharField(max_length=255, blank=True)
    valor = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    fabricante = models.CharField(max_length=255, blank=True)
    fornecedor = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'TabInsumo'


class Tabitensexp(models.Model):
    cdie = models.IntegerField(primary_key=True)
    cdproduto = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    quantidade = models.IntegerField(
        db_column='Quantidade', blank=True, null=True)
    usuario = models.CharField(max_length=255, blank=True)
    datai = models.DateTimeField(blank=True, null=True)
    cd_oe = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'TabItensExp'


class Tabkit(models.Model):
    cd_kit = models.IntegerField(primary_key=True)
    cd_produto = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    quantidade = models.IntegerField(
        db_column='Quantidade', blank=True, null=True)
    usuario = models.CharField(max_length=255, blank=True)
    datae = models.DateTimeField(blank=True, null=True)
    datai = models.DateTimeField(blank=True, null=True)
    matricula = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'TabKit'


class Tabkitrec(models.Model):
    # Field name made lowercase.
    cd_kitrec = models.IntegerField(db_column='cd_kitRec', primary_key=True)
    cd_produto = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    quantidade = models.IntegerField(
        db_column='Quantidade', blank=True, null=True)
    usuario = models.CharField(max_length=255, blank=True)
    datar = models.DateTimeField(blank=True, null=True)
    datai = models.DateTimeField(blank=True, null=True)
    matricula = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'TabKitRec'


class Tabmensagens(models.Model):
    codmsg = models.IntegerField(primary_key=True)
    emitente = models.CharField(max_length=255, blank=True)
    destinatario = models.CharField(max_length=255, blank=True)
    msg = models.TextField(blank=True)
    datae = models.DateTimeField(blank=True, null=True)
    recebido = models.IntegerField(blank=True, null=True)
    enviado = models.IntegerField(blank=True, null=True)
    datar = models.DateTimeField(blank=True, null=True)
    lido = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TabMensagens'


class Tabmunicipios(models.Model):
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    identifica_o = models.IntegerField(
        db_column='Identifica\xe7\xe3o', primary_key=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    pa_ses = models.CharField(
        db_column='Pa\xedses', max_length=765, blank=True)
    # Field name made lowercase.
    estados = models.CharField(db_column='Estados', max_length=255, blank=True)
    # Field name made lowercase.
    siglae = models.CharField(db_column='SiglaE', max_length=2, blank=True)
    # Field name made lowercase.
    cidades = models.CharField(db_column='Cidades', max_length=255, blank=True)
    # Field name made lowercase.
    nacionalidade = models.CharField(
        db_column='Nacionalidade', max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'TabMunicipios'


class Tabnomeacoes(models.Model):
    # Field name made lowercase.
    codnomea = models.IntegerField(db_column='Codnomea', primary_key=True)
    # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=11, blank=True)
    # Field name made lowercase.
    matricula = models.CharField(db_column='Matricula', max_length=50)
    # Field name made lowercase.
    df = models.CharField(db_column='DF', max_length=255, blank=True)
    # Field name made lowercase.
    descdf = models.CharField(db_column='DescDF', max_length=50, blank=True)
    # Field name made lowercase.
    dodf = models.IntegerField(db_column='DODF', blank=True, null=True)
    # Field name made lowercase.
    pag = models.IntegerField(db_column='Pag', blank=True, null=True)
    # Field name made lowercase.
    datadodf = models.DateTimeField(
        db_column='DatadoDF', blank=True, null=True)
    # Field name made lowercase.
    datanomeacao = models.DateTimeField(
        db_column='Datanomeacao', blank=True, null=True)
    # Field name made lowercase.
    dataposse = models.DateTimeField(
        db_column='DataPosse', blank=True, null=True)
    # Field name made lowercase.
    dataexercicio = models.DateTimeField(
        db_column='DataExercicio', blank=True, null=True)
    # Field name made lowercase.
    atonomea = models.CharField(
        db_column='Atonomea', max_length=255, blank=True)
    # Field name made lowercase.
    dataexoneracao = models.DateTimeField(
        db_column='DataExoneracao', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TabNomeacoes'


class Taboa(models.Model):
    cd_oa = models.IntegerField(primary_key=True)
    cd_produto = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    quantidade = models.IntegerField(
        db_column='Quantidade', blank=True, null=True)
    usuario = models.CharField(max_length=255, blank=True)
    dataa = models.DateTimeField(blank=True, null=True)
    datai = models.DateTimeField(blank=True, null=True)
    cdentidade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TabOA'


class Taboe(models.Model):
    cd_oe = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=255, blank=True)
    dataexp = models.DateTimeField(blank=True, null=True)
    cdlocalexp = models.IntegerField(blank=True, null=True)
    finalidade = models.CharField(max_length=255, blank=True)
    estampa = models.CharField(max_length=255, blank=True)
    demandante = models.CharField(max_length=255, blank=True)
    cdsublocal = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'TabOE'


class Tabof(models.Model):
    cd_of = models.IntegerField(primary_key=True)
    data = models.DateTimeField(blank=True, null=True)
    usuario = models.CharField(max_length=255, blank=True)
    cd_produto = models.IntegerField(blank=True, null=True)
    qtde_produto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TabOF'


class Tabop(models.Model):
    cd_op = models.IntegerField(primary_key=True)
    cd_etapa = models.IntegerField(blank=True, null=True)
    tipop = models.CharField(max_length=255, blank=True)
    matricula = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True)
    # Field name made lowercase.
    quantidadeq = models.IntegerField(
        db_column='Quantidadeq', blank=True, null=True)
    usuario = models.CharField(max_length=255, blank=True)
    dataop = models.DateTimeField(blank=True, null=True)
    valorq = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    valoretapa = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    cd_kitrec = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TabOP'


class Tabps(models.Model):
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    c_digo = models.IntegerField(db_column='C\xf3digo', primary_key=True)
    # Field name made lowercase.
    ps = models.CharField(db_column='PS', max_length=255, blank=True)
    # Field name made lowercase.
    razao = models.CharField(db_column='Razao', max_length=255, blank=True)
    # Field name made lowercase.
    cnpj = models.FloatField(db_column='CNPJ', blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True)
    municipio = models.CharField(max_length=255, blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    cep = models.FloatField(blank=True, null=True)
    # Field name made lowercase.
    tcomercial = models.FloatField(
        db_column='Tcomercial', blank=True, null=True)
    # Field name made lowercase.
    tfax = models.FloatField(db_column='TFax', blank=True, null=True)
    # Field name made lowercase.
    tcelular = models.FloatField(db_column='TCelular', blank=True, null=True)
    # Field name made lowercase.
    responsavel = models.CharField(
        db_column='Responsavel', max_length=255, blank=True)
    # Field name made lowercase.
    qf = models.IntegerField(db_column='QF', blank=True, null=True)
    # Field name made lowercase.
    qm = models.IntegerField(db_column='QM', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TabPS'


class Tabpessoais(models.Model):
    # Field name made lowercase.
    codpessoal = models.IntegerField(db_column='CODPESSOAL', primary_key=True)
    # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True)
    # Field name made lowercase.
    nomepai = models.CharField(db_column='NomePai', max_length=255, blank=True)
    # Field name made lowercase.
    nomemae = models.CharField(db_column='NomeMae', max_length=255, blank=True)
    # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=50, blank=True)
    # Field name made lowercase.
    estadocivil = models.CharField(
        db_column='EstadoCivil', max_length=50, blank=True)
    # Field name made lowercase.
    datanascimento = models.DateTimeField(
        db_column='DataNascimento', blank=True, null=True)
    # Field name made lowercase.
    cartestrangeiro = models.CharField(
        db_column='CartEstrangeiro', max_length=255, blank=True)
    # Field name made lowercase.
    pispasep = models.FloatField(db_column='PISPasep', blank=True, null=True)
    # Field name made lowercase.
    dtpis = models.DateTimeField(db_column='DtPis', blank=True, null=True)
    # Field name made lowercase.
    matricula = models.CharField(
        db_column='Matricula', unique=True, max_length=50, blank=True)
    # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', unique=True, max_length=11)
    # Field name made lowercase.
    rg = models.CharField(db_column='RG', max_length=50, blank=True)
    # Field name made lowercase.
    orgaoexpedidor = models.CharField(
        db_column='OrgaoExpedidor', max_length=50, blank=True)
    # Field name made lowercase.
    ufexp = models.CharField(db_column='UFexp', max_length=2, blank=True)
    # Field name made lowercase.
    dataexp = models.DateTimeField(db_column='DataExp', blank=True, null=True)
    # Field name made lowercase.
    tituloeleitor = models.FloatField(
        db_column='TituloEleitor', blank=True, null=True)
    # Field name made lowercase.
    zonat = models.IntegerField(db_column='Zonat', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    se_ot = models.IntegerField(
        db_column='Se\xe7\xe3ot', blank=True, null=True)
    # Field name made lowercase.
    municipiot = models.CharField(
        db_column='Municipiot', max_length=255, blank=True)
    # Field name made lowercase.
    uft = models.CharField(db_column='UFt', max_length=255, blank=True)
    # Field name made lowercase.
    endereco = models.CharField(
        db_column='Endereco', max_length=255, blank=True)
    # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=50, blank=True)
    # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=2, blank=True)
    # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=50, blank=True)
    # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=50, blank=True)
    # Field name made lowercase.
    telefoneres = models.CharField(
        db_column='TelefoneRes', max_length=50, blank=True)
    # Field name made lowercase.
    telefonecelular = models.CharField(
        db_column='TelefoneCelular', max_length=50, blank=True)
    # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True)
    # Field name made lowercase.
    filhos = models.IntegerField(db_column='Filhos', blank=True, null=True)
    # Field name made lowercase.
    pne = models.IntegerField(db_column='PNE', blank=True, null=True)
    # Field name made lowercase.
    qualdef = models.CharField(db_column='QualDef', max_length=255, blank=True)
    # Field name made lowercase.
    nac = models.CharField(db_column='Nac', max_length=255, blank=True)
    # Field name made lowercase.
    paisorigem = models.CharField(
        db_column='PaisOrigem', max_length=255, blank=True)
    # Field name made lowercase.
    nat = models.CharField(db_column='Nat', max_length=255, blank=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    ra_a = models.CharField(db_column='Ra\xe7a', max_length=765, blank=True)
    habitacao = models.CharField(max_length=255, blank=True)
    # Field name made lowercase.
    cnh = models.FloatField(db_column='CNH', blank=True, null=True)
    # Field name made lowercase.
    ufcnh = models.CharField(db_column='UFcnh', max_length=2, blank=True)
    # Field name made lowercase.
    categoria = models.CharField(
        db_column='Categoria', max_length=3, blank=True)
    datacnh = models.DateTimeField(blank=True, null=True)
    validadecnh = models.DateTimeField(blank=True, null=True)
    # Field name made lowercase.
    creserva = models.FloatField(db_column='Creserva', blank=True, null=True)
    # Field name made lowercase.
    seriecr = models.IntegerField(db_column='SerieCR', blank=True, null=True)
    orgaocr = models.CharField(max_length=2, blank=True)
    # Field name made lowercase.
    categoriacr = models.CharField(
        db_column='CategoriaCR', max_length=255, blank=True)
    # Field name made lowercase.
    anoservico = models.IntegerField(
        db_column='AnoServico', blank=True, null=True)
    # Field name made lowercase.
    cdi = models.IntegerField(db_column='CDI', blank=True, null=True)
    # Field name made lowercase.
    umilitar = models.CharField(db_column='UMilitar', max_length=8, blank=True)
    # Field name made lowercase.
    ufservico = models.CharField(
        db_column='UFservico', max_length=2, blank=True)
    # Field name made lowercase.
    cc = models.IntegerField(db_column='CC', blank=True, null=True)
    # Field name made lowercase.
    banco = models.IntegerField(db_column='Banco', blank=True, null=True)
    # Field name made lowercase.
    agencia = models.IntegerField(db_column='Agencia', blank=True, null=True)
    # Field name made lowercase.
    ts = models.CharField(db_column='TS', max_length=255, blank=True)
    anochegada = models.CharField(max_length=4, blank=True)
    conjuge = models.CharField(max_length=255, blank=True)
    # Field name made lowercase.
    localfoto = models.CharField(
        db_column='LocalFoto', max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'TabPessoais'


class Tabproduto(models.Model):
    cd_produto = models.IntegerField(primary_key=True)
    # Field name made lowercase.
    produto = models.CharField(db_column='Produto', max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'TabProduto'


class Tabprodutoinsumo(models.Model):
    cd_pi = models.IntegerField(primary_key=True)
    cd_insumo = models.IntegerField(blank=True, null=True)
    qtd = models.FloatField(blank=True, null=True)
    medida = models.CharField(max_length=255, blank=True)
    cd_produto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TabProdutoInsumo'


class Tabreqat(models.Model):
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    c_digo = models.IntegerField(db_column='C\xf3digo', primary_key=True)
    # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=11)
    nome = models.CharField(max_length=255, blank=True)
    cargo = models.CharField(max_length=255, blank=True)
    classe = models.CharField(max_length=255, blank=True)
    padrao = models.CharField(max_length=255, blank=True)
    lotacao = models.CharField(max_length=255, blank=True)
    endfunc = models.CharField(max_length=255, blank=True)
    endres = models.CharField(max_length=255, blank=True)
    telfunc = models.CharField(max_length=255, blank=True)
    cep = models.CharField(max_length=255, blank=True)
    bairro = models.CharField(max_length=255, blank=True)
    uf = models.CharField(max_length=255, blank=True)
    cidade = models.CharField(max_length=255, blank=True)
    tel = models.CharField(max_length=255, blank=True)
    inclusao = models.IntegerField(blank=True, null=True)
    alteracao = models.IntegerField(blank=True, null=True)
    exclusao = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    matricula = models.IntegerField(db_column='Matricula')
    linhaida1 = models.IntegerField(blank=True, null=True)
    tarifalinhaida1 = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    linhaida2 = models.IntegerField(blank=True, null=True)
    tarifalinhaida2 = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    linhaida3 = models.IntegerField(blank=True, null=True)
    tarifalinhaida3 = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    linhavolta1 = models.IntegerField(blank=True, null=True)
    tarifalinhavolta1 = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    linhavolta2 = models.IntegerField(blank=True, null=True)
    tarifalinhavolta2 = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    linhavolta3 = models.IntegerField(blank=True, null=True)
    tarifalinhavolta3 = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    cd = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    plant_o = models.IntegerField(
        db_column='plant\xe3o', blank=True, null=True)
    escala = models.CharField(max_length=255, blank=True)
    datasolicitacao = models.DateTimeField(blank=True, null=True)
    dataregistro = models.DateTimeField(blank=True, null=True)
    incluido = models.IntegerField(blank=True, null=True)
    excluido = models.IntegerField(blank=True, null=True)
    alterado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TabReqAT'


class Tabsubproduto(models.Model):
    cd_subproduto = models.IntegerField(primary_key=True)
    subproduto = models.CharField(max_length=255, blank=True)
    cd_produto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TabSubProduto'


class Tabtipofuncao(models.Model):
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    c_digo = models.IntegerField(db_column='C\xf3digo', primary_key=True)
    # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'TabTipoFunção'


class Tabtipoproduto(models.Model):
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    c_digo = models.IntegerField(db_column='C\xf3digo', primary_key=True)
    # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=255, blank=True)
    # Field name made lowercase.
    descricao = models.CharField(
        db_column='Descricao', max_length=255, blank=True)
    # Field name made lowercase.
    formato = models.CharField(db_column='Formato', max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'TabTipoProduto'


class Tabtipolinhas(models.Model):
    cd_linha = models.IntegerField(primary_key=True)
    linha = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    descricao = models.CharField(
        db_column='Descricao', max_length=255, blank=True)
    tipo = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'TabTipolinhas'


class Tabtiposoe(models.Model):
    # Field name made lowercase.
    codigoi = models.CharField(
        db_column='CODIGOI', primary_key=True, max_length=255)
    # Field name made lowercase.
    descricao = models.CharField(
        db_column='DESCRICAO', max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'TabTiposOE'


class TabDocumento(models.Model):
    # Field name made lowercase.
    coddocumento = models.IntegerField(
        db_column='CodDocumento', primary_key=True)
    # Field name made lowercase.
    documento = models.CharField(
        db_column='Documento', max_length=150, blank=True)

    class Meta:
        managed = False
        db_table = 'Tab_documento'


class Tababonos(models.Model):
    # Field name made lowercase.
    codigoabono = models.IntegerField(
        db_column='CodigoAbono', primary_key=True)
    # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=11)
    # Field name made lowercase.
    matricula = models.CharField(
        db_column='Matricula', max_length=50, blank=True)
    # Field name made lowercase.
    anoexercicio = models.CharField(
        db_column='AnoExercicio', max_length=255, blank=True)
    # Field name made lowercase.
    abono1 = models.DateTimeField(db_column='Abono1', blank=True, null=True)
    # Field name made lowercase.
    abono1f = models.DateTimeField(db_column='Abono1f', blank=True, null=True)
    # Field name made lowercase.
    gozado1 = models.IntegerField(db_column='Gozado1', blank=True, null=True)
    # Field name made lowercase.
    abono2 = models.DateTimeField(db_column='Abono2', blank=True, null=True)
    # Field name made lowercase.
    abono2f = models.DateTimeField(db_column='Abono2f', blank=True, null=True)
    # Field name made lowercase.
    gozado2 = models.IntegerField(db_column='Gozado2', blank=True, null=True)
    # Field name made lowercase.
    abono3 = models.DateTimeField(db_column='Abono3', blank=True, null=True)
    # Field name made lowercase.
    abono3f = models.DateTimeField(db_column='Abono3f', blank=True, null=True)
    # Field name made lowercase.
    gozado3 = models.IntegerField(db_column='Gozado3', blank=True, null=True)
    # Field name made lowercase.
    abono4 = models.DateTimeField(db_column='Abono4', blank=True, null=True)
    # Field name made lowercase.
    abono4f = models.DateTimeField(db_column='Abono4f', blank=True, null=True)
    # Field name made lowercase.
    gozado4 = models.IntegerField(db_column='Gozado4', blank=True, null=True)
    # Field name made lowercase.
    abono5 = models.DateTimeField(db_column='Abono5', blank=True, null=True)
    # Field name made lowercase.
    abono5f = models.DateTimeField(db_column='Abono5f', blank=True, null=True)
    # Field name made lowercase.
    gozado5 = models.IntegerField(db_column='Gozado5', blank=True, null=True)
    # Field name made lowercase.
    obs = models.TextField(db_column='Obs', blank=True)
    # Field name made lowercase.
    plantao2472 = models.IntegerField(
        db_column='Plantao2472', blank=True, null=True)
    # Field name made lowercase.
    plantao1236 = models.IntegerField(
        db_column='Plantao1236', blank=True, null=True)
    dtsolicitacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tababonos'


class Tabes(models.Model):
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    c_digo = models.IntegerField(db_column='C\xf3digo', primary_key=True)
    radio = models.IntegerField(blank=True, null=True)
    tv = models.IntegerField(blank=True, null=True)
    mlr = models.IntegerField(blank=True, null=True)
    geladeira = models.IntegerField(blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    fixo = models.IntegerField(blank=True, null=True)
    computador = models.IntegerField(blank=True, null=True)
    cnet = models.IntegerField(blank=True, null=True)
    moto = models.IntegerField(blank=True, null=True)
    automovel = models.IntegerField(blank=True, null=True)
    numpessoas = models.IntegerField(blank=True, null=True)
    responsabilidade1 = models.IntegerField(blank=True, null=True)
    responsabilidade2 = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    nnm = models.CharField(db_column='Nnm', max_length=255, blank=True)
    # Field name made lowercase.
    nuf = models.CharField(db_column='Nuf', max_length=255, blank=True)
    # Field renamed to remove unsuitable characters.
    interrup_o = models.IntegerField(
        db_column='interrup\xe7\xe3o', blank=True, null=True)
    # Field name made lowercase.
    fe = models.CharField(db_column='FE', max_length=255, blank=True)
    # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=11)
    sle = models.CharField(max_length=255, blank=True)
    # Field name made lowercase.
    escolaridade = models.CharField(
        db_column='Escolaridade', max_length=50, blank=True)
    ano = models.CharField(max_length=255, blank=True)
    dtatualiza = models.DateTimeField(blank=True, null=True)
    totalrend = models.CharField(max_length=255, blank=True)
    habitacao = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'Tabes'


class Tabferias(models.Model):
    # Field name made lowercase.
    codigoferias = models.IntegerField(
        db_column='CodigoFerias', primary_key=True)
    # Field name made lowercase.
    anoexercicio = models.CharField(
        db_column='AnoExercicio', max_length=4, blank=True)
    # Field name made lowercase.
    anogozo = models.CharField(db_column='AnoGozo', max_length=4, blank=True)
    # Field name made lowercase.
    mes = models.CharField(db_column='Mes', max_length=50, blank=True)
    # Field name made lowercase.
    mes1 = models.CharField(db_column='Mes1', max_length=50, blank=True)
    # Field name made lowercase.
    mes2 = models.CharField(db_column='Mes2', max_length=50, blank=True)
    # Field name made lowercase.
    mes3 = models.CharField(db_column='Mes3', max_length=50, blank=True)
    # Field name made lowercase.
    pi = models.DateTimeField(db_column='PI', blank=True, null=True)
    # Field name made lowercase.
    pf = models.DateTimeField(db_column='PF', blank=True, null=True)
    # Field name made lowercase.
    pi1 = models.DateTimeField(db_column='PI1', blank=True, null=True)
    # Field name made lowercase.
    pf1 = models.DateTimeField(db_column='PF1', blank=True, null=True)
    # Field name made lowercase.
    pi2 = models.DateTimeField(db_column='PI2', blank=True, null=True)
    # Field name made lowercase.
    pf2 = models.DateTimeField(db_column='PF2', blank=True, null=True)
    # Field name made lowercase.
    pi3 = models.DateTimeField(db_column='PI3', blank=True, null=True)
    # Field name made lowercase.
    pf3 = models.DateTimeField(db_column='PF3', blank=True, null=True)
    # Field name made lowercase.
    datasolicitacao = models.DateTimeField(
        db_column='DataSolicitacao', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    situa_osolicita_o = models.CharField(
        db_column='Situa\xe7\xe3oSolicita\xe7\xe3o', max_length=150, blank=True)
    # Field name made lowercase.
    feriasparc = models.IntegerField(
        db_column='FeriasParc', blank=True, null=True)
    # Field name made lowercase.
    adiant = models.IntegerField(db_column='Adiant', blank=True, null=True)
    # Field name made lowercase.
    matricula = models.CharField(db_column='Matricula', max_length=50)
    # Field name made lowercase.
    obsf = models.TextField(db_column='Obsf', blank=True)
    # Field name made lowercase.
    remarcar = models.IntegerField(db_column='Remarcar', blank=True, null=True)
    # Field name made lowercase.
    dtcancel = models.DateTimeField(
        db_column='DTCANCEL', blank=True, null=True)
    # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=11)

    class Meta:
        managed = False
        db_table = 'Tabferias'


class Tabfuncao(models.Model):
    # Field name made lowercase.
    funcao = models.CharField(
        db_column='Funcao', primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'Tabfuncao'


class Tabtipoafasta(models.Model):
    # Field name made lowercase.
    codigo = models.IntegerField(db_column='CODIGO', primary_key=True)
    # Field name made lowercase.
    descricao = models.CharField(
        db_column='DESCRICAO', max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'Tabtipoafasta'


class Tabtipolota(models.Model):
    # Field name made lowercase.
    codlotacao = models.CharField(
        db_column='CodLotacao', primary_key=True, max_length=50)
    # Field name made lowercase.
    nomel = models.CharField(db_column='Nomel', max_length=70, blank=True)
    sigla = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'Tabtipolota'


class Tabtipoorgaocr(models.Model):
    # Field name made lowercase.
    sigla = models.CharField(db_column='SIGLA', primary_key=True, max_length=2)
    # Field name made lowercase.
    descricao = models.CharField(
        db_column='DESCRICAO', max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'TabtipoorgaoCR'


class Tabtipoparentesco(models.Model):
    codpar = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'Tabtipoparentesco'


class Tabtiposcc(models.Model):
    # Field name made lowercase.
    coddf = models.CharField(
        db_column='CodDF', primary_key=True, max_length=50)
    # Field name made lowercase.
    descricaodf = models.CharField(
        db_column='DescricaoDF', max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'TabtiposCC'


class Tabtiposce(models.Model):
    # Field name made lowercase.
    ceftivo = models.CharField(
        db_column='Ceftivo', primary_key=True, max_length=255)
    # Field name made lowercase.
    codcargo = models.CharField(
        db_column='CodCargo', max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'TabtiposCE'


class Tabtiposhabitacao(models.Model):
    # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'TabtiposHabitacao'


class Tabtiposoo(models.Model):
    # Field name made lowercase.
    codorgaoorigem = models.IntegerField(
        db_column='CodOrgaoOrigem', primary_key=True)
    # Field name made lowercase.
    nomeo = models.CharField(db_column='NomeO', max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'TabtiposOO'


class Tabusuarios(models.Model):
    # Field name made lowercase.
    iduser = models.IntegerField(db_column='Iduser', unique=True)
    usuario = models.CharField(max_length=255, blank=True)
    # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True)
    # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=4, blank=True)
    # Field name made lowercase.
    nucleo = models.CharField(db_column='Nucleo', max_length=255, blank=True)
    # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', unique=True, max_length=11)
    status = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'Tabusuarios'


class Tbimagemcap(models.Model):
    cdimagem = models.IntegerField(primary_key=True)
    matricula = models.IntegerField(blank=True, null=True)
    localfoto = models.CharField(max_length=255, blank=True)
    autorizado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TbImagemCap'


class Tbprodutoinsumo(models.Model):
    cd_pi = models.IntegerField(primary_key=True)
    cd_insumo = models.IntegerField(blank=True, null=True)
    qtd = models.FloatField(blank=True, null=True)
    medida = models.CharField(max_length=255, blank=True)
    cd_produto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TbProdutoInsumo'


class Tbetapa(models.Model):
    cd_etapa = models.IntegerField(primary_key=True)
    etapa = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'Tbetapa'


class Tbproduto(models.Model):
    cd_produto = models.IntegerField(primary_key=True)
    # Field name made lowercase.
    produto = models.CharField(db_column='Produto', max_length=255, blank=True)
    tipo = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'Tbproduto'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey(
        'DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Tbarquivoreg(models.Model):
    cdarquivo = models.IntegerField(primary_key=True)
    cdfacepasta = models.IntegerField(blank=True, null=True)
    usuario = models.CharField(max_length=255, blank=True)
    diai = models.DateTimeField(blank=True, null=True)
    horai = models.DateTimeField(blank=True, null=True)
    alterado = models.IntegerField(blank=True, null=True)
    matricula = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbArquivoReg'


class Tbassiduidade(models.Model):
    cda = models.IntegerField(primary_key=True)
    matricula = models.IntegerField(blank=True, null=True)
    datar = models.DateTimeField(blank=True, null=True)
    horar = models.DateTimeField(blank=True, null=True)
    horar2 = models.DateTimeField(blank=True, null=True)
    horar3 = models.DateTimeField(blank=True, null=True)
    horar4 = models.DateTimeField(blank=True, null=True)
    motivo = models.CharField(max_length=255, blank=True)
    usuario = models.CharField(max_length=255, blank=True)
    datai = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbAssiduidade'


class Tbcadeado(models.Model):
    cd_cadeado = models.IntegerField(primary_key=True)
    numero = models.IntegerField(blank=True, null=True)
    disponivel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbCadeado'


class Tbcadeadoreg(models.Model):
    cdarquivo = models.IntegerField(primary_key=True)
    cd_cadeado = models.IntegerField(blank=True, null=True)
    usuario = models.CharField(max_length=255, blank=True)
    diai = models.DateTimeField(blank=True, null=True)
    horai = models.DateTimeField(blank=True, null=True)
    alterado = models.IntegerField(blank=True, null=True)
    matricula = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbCadeadoReg'


class Tbentidades(models.Model):
    cdentidade = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255, blank=True)
    # Field name made lowercase.
    cnpj = models.FloatField(db_column='CNPJ', blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True)
    municipio = models.CharField(max_length=255, blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    cep = models.CharField(max_length=8, blank=True)
    # Field name made lowercase.
    tcomercial = models.CharField(
        db_column='Tcomercial', max_length=10, blank=True)
    # Field name made lowercase.
    tfax = models.CharField(db_column='TFax', max_length=10, blank=True)
    # Field name made lowercase.
    tcelular = models.CharField(
        db_column='TCelular', max_length=10, blank=True)
    email = models.CharField(max_length=255, blank=True)
    # Field name made lowercase.
    responsavel = models.CharField(
        db_column='Responsavel', max_length=255, blank=True)
    tipoentidade = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'tbEntidades'


class Tbmaquina(models.Model):
    cdmaquina = models.IntegerField(primary_key=True)
    maquina = models.CharField(max_length=255, blank=True)
    usuario = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'tbMaquina'


class Tbvalorlinha(models.Model):
    cd_vlinha = models.IntegerField(primary_key=True)
    tipo = models.CharField(unique=True, max_length=255, blank=True)
    # Field name made lowercase.
    valor = models.DecimalField(
        db_column='Valor', max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbValorLinha'


class Tbbens(models.Model):
    cdbens = models.IntegerField(primary_key=True)
    cpf = models.CharField(max_length=255, blank=True)
    bem = models.CharField(max_length=255, blank=True)
    valor = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbbens'


class Tbce(models.Model):
    cdce = models.IntegerField(primary_key=True)
    codigo = models.IntegerField(blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'tbce'


class Tbdoc(models.Model):
    cddoc = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=255, blank=True)
    prefixo = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    assunto = models.CharField(max_length=255, blank=True)
    data = models.DateTimeField(blank=True, null=True)
    validade = models.DateTimeField(blank=True, null=True)
    gestor = models.CharField(max_length=255, blank=True)
    localdoc = models.CharField(max_length=255, blank=True)
    situacao = models.CharField(max_length=255, blank=True)
    usuario = models.CharField(max_length=255, blank=True)
    datar = models.DateTimeField(blank=True, null=True)
    demandante = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'tbdoc'


class Tbdocumento(models.Model):
    cd_doc = models.IntegerField(primary_key=True)
    doc = models.CharField(unique=True, max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'tbdocumento'


class Tbdtpag(models.Model):
    cddtpag = models.IntegerField(primary_key=True)
    ano = models.CharField(max_length=255, blank=True)
    mes = models.CharField(max_length=255, blank=True)
    dti = models.DateTimeField(blank=True, null=True)
    dtf = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbdtpag'


class Tbelemento(models.Model):
    cde = models.IntegerField(primary_key=True)
    codigo = models.IntegerField(blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'tbelemento'


class Tbfacepasta(models.Model):
    cdfacepasta = models.IntegerField(primary_key=True)
    face = models.IntegerField(blank=True, null=True)
    pasta = models.IntegerField(blank=True, null=True)
    ocupada = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbfacepasta'


class Tbfolhap(models.Model):
    cdfp = models.IntegerField(primary_key=True)
    matricula = models.IntegerField(blank=True, null=True)
    aai = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    pia = models.IntegerField(blank=True, null=True)
    ia = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    pa = models.IntegerField(blank=True, null=True)
    aa = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    cd = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    pt = models.IntegerField(blank=True, null=True)
    at = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    mes = models.CharField(max_length=255, blank=True)
    ano = models.CharField(max_length=255, blank=True)
    nfolha = models.IntegerField(blank=True, null=True)
    diasu = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbfolhap'


class Tbgentrada(models.Model):
    cd_gruia = models.IntegerField(primary_key=True)
    n_guia = models.IntegerField(unique=True, blank=True, null=True)
    dt_criacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbgentrada'


class Tbgnd(models.Model):
    cdgnd = models.IntegerField(primary_key=True)
    codigo = models.IntegerField(blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'tbgnd'


class Tbgsaida(models.Model):
    cd_gruia = models.IntegerField(primary_key=True)
    n_guia = models.IntegerField(unique=True, blank=True, null=True)
    dt_criacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbgsaida'


class Tbif(models.Model):
    cdif = models.IntegerField(primary_key=True)
    cddoc = models.IntegerField(blank=True, null=True)
    folhade = models.IntegerField(blank=True, null=True)
    folhaa = models.IntegerField(blank=True, null=True)
    usuario = models.CharField(max_length=255, blank=True)
    data = models.DateTimeField(blank=True, null=True)
    localfolha = models.CharField(max_length=255, blank=True)
    volume = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbif'


class Tbinscricao(models.Model):
    cd_inscricao = models.IntegerField(unique=True)
    nome = models.CharField(max_length=255, blank=True)
    cpf = models.CharField(max_length=11, blank=True)
    # Field name made lowercase.
    pcd = models.IntegerField(db_column='PCD', blank=True, null=True)
    # Field name made lowercase.
    acl = models.IntegerField(db_column='ACL', blank=True, null=True)
    idoso = models.IntegerField(blank=True, null=True)
    deficiencia = models.CharField(max_length=255, blank=True)
    datai = models.DateTimeField(blank=True, null=True)
    horai = models.DateTimeField(blank=True, null=True)
    usuarioi = models.CharField(max_length=255, blank=True)
    sorteado = models.IntegerField(blank=True, null=True)
    cadreserva = models.IntegerField(blank=True, null=True)
    tel01 = models.CharField(max_length=255, blank=True)
    tel02 = models.CharField(max_length=255, blank=True)
    satelite = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'tbinscricao'


class Tbinsumo(models.Model):
    cd_insumo = models.IntegerField(primary_key=True)
    insumo = models.CharField(max_length=255, blank=True)
    medida = models.CharField(max_length=255, blank=True)
    valor = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    fabricante = models.CharField(max_length=255, blank=True)
    fornecedor = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'tbinsumo'


class Tblog(models.Model):
    # Field name made lowercase.
    id_log = models.IntegerField(db_column='ID', blank=True, null=True)
    # Field name made lowercase.
    cpoalterado = models.CharField(
        db_column='CpoAlterado', max_length=255, blank=True)
    # Field name made lowercase.
    alteradode = models.TextField(db_column='AlteradoDe', blank=True)
    # Field name made lowercase.
    alteradopara = models.TextField(db_column='AlteradoPara', blank=True)
    # Field name made lowercase.
    formulario = models.CharField(
        db_column='Formulario', max_length=50, blank=True)
    # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=255, blank=True)
    # Field name made lowercase.
    maquina = models.CharField(db_column='Maquina', max_length=50, blank=True)
    # Field name made lowercase.
    dataalt = models.DateTimeField(db_column='DataAlt', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblog'


class Tbma(models.Model):
    cdma = models.IntegerField(primary_key=True)
    codigo = models.IntegerField(blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'tbma'


class Tbobjeto(models.Model):
    cdob = models.IntegerField(primary_key=True)
    objeto = models.CharField(max_length=255, blank=True)
    usuario = models.CharField(max_length=255, blank=True)
    modalidade = models.CharField(max_length=255, blank=True)
    tipol = models.CharField(max_length=255, blank=True)
    grupo = models.IntegerField(blank=True, null=True)
    modalidadea = models.IntegerField(blank=True, null=True)
    elemento = models.IntegerField(blank=True, null=True)
    subelemento = models.IntegerField(blank=True, null=True)
    previsao = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    ce = models.IntegerField(blank=True, null=True)
    datar = models.DateTimeField(blank=True, null=True)
    cddoc = models.IntegerField(blank=True, null=True)
    valorneg = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbobjeto'


class Tbpainel(models.Model):
    cdsenha = models.IntegerField(primary_key=True)
    mesa = models.IntegerField(blank=True, null=True)
    senha = models.IntegerField(blank=True, null=True)
    datas = models.DateTimeField(blank=True, null=True)
    horas = models.DateTimeField(blank=True, null=True)
    usuario = models.CharField(max_length=255, blank=True)
    resposta = models.CharField(max_length=255, blank=True)
    enviado = models.IntegerField(blank=True, null=True)
    horaa = models.DateTimeField(blank=True, null=True)
    exibida = models.IntegerField(blank=True, null=True)
    rechamada = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbpainel'


class Tbpentrada(models.Model):
    cd_protocolo = models.IntegerField(primary_key=True)
    n_protocolo = models.IntegerField(blank=True, null=True)
    doc = models.CharField(max_length=255, blank=True)
    ano_doc = models.IntegerField(blank=True, null=True)
    prefixo = models.IntegerField(blank=True, null=True)
    n_doc = models.IntegerField(blank=True, null=True)
    interessado = models.CharField(max_length=255, blank=True)
    assunto = models.TextField(blank=True)
    de_onde = models.CharField(max_length=255, blank=True)
    setor = models.CharField(max_length=255, blank=True)
    responsavel = models.CharField(max_length=255, blank=True)
    matricula = models.CharField(max_length=8, blank=True)
    dt_recebe = models.DateTimeField(blank=True, null=True)
    n_guia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbpentrada'


class Tbprodutoetapa(models.Model):
    cdpe = models.IntegerField(primary_key=True)
    cd_etapa = models.IntegerField(blank=True, null=True)
    cd_produto = models.IntegerField(blank=True, null=True)
    tipoproduto = models.CharField(max_length=255, blank=True)
    valor = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbprodutoetapa'


class Tbpsaida(models.Model):
    cd_protocolo = models.IntegerField(primary_key=True)
    n_protocolo = models.IntegerField(blank=True, null=True)
    doc = models.CharField(max_length=255, blank=True)
    ano_doc = models.IntegerField(blank=True, null=True)
    prefixo = models.IntegerField(blank=True, null=True)
    n_doc = models.IntegerField(blank=True, null=True)
    interessado = models.CharField(max_length=255, blank=True)
    assunto = models.TextField(blank=True)
    de_onde = models.CharField(max_length=255, blank=True)
    setor = models.CharField(max_length=255, blank=True)
    responsavel = models.CharField(max_length=255, blank=True)
    matricula = models.CharField(max_length=8, blank=True)
    dt_saida = models.DateTimeField(blank=True, null=True)
    n_guia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbpsaida'


class Tbresiduos(models.Model):
    cdresiduo = models.IntegerField(primary_key=True)
    entidade = models.CharField(max_length=255, blank=True)
    oficio = models.CharField(max_length=255, blank=True)
    datae = models.DateTimeField(blank=True, null=True)
    datai = models.DateTimeField(blank=True, null=True)
    qtdedoadapv = models.IntegerField(blank=True, null=True)
    qtdedoadatergal = models.IntegerField(blank=True, null=True)
    qtdedoadaeva = models.IntegerField(blank=True, null=True)
    qtdedoadaribana = models.IntegerField(blank=True, null=True)
    qtdedoadabrim = models.IntegerField(blank=True, null=True)
    qtdedoadacarreteis = models.IntegerField(blank=True, null=True)
    qtdedoadamp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbresiduos'


class Tbsube(models.Model):
    cdse = models.IntegerField(primary_key=True)
    codigo = models.IntegerField(blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True)
    cde = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbsube'
