
from __future__ import unicode_literals

from django.db import models


class AreaAtuacao(models.Model):
    idareaatuacao = models.IntegerField(
        db_column='idAreaAtuacao',
        primary_key=True)

    nome = models.CharField(
        max_length=255,
        blank=True)

    class Meta:
        managed = False
        db_table = 'AreaAtuacao'


class CNH(models.Model):
    idcnh = models.IntegerField(
        db_column='idCNH')

    numero = models.BigIntegerField()

    dataemissao = models.DateField(
        db_column='dataEmissao',
        blank=True,
        null=True)

    validade = models.DateField(
        blank=True, null=True)

    uf = models.ForeignKey('UF', db_column='UF')

    categoriacnh = models.ForeignKey(
        'CategoriaCNH', db_column='CategoriaCNH')

    pessoa = models.ForeignKey(
        'Pessoa', db_column='Pessoa')

    class Meta:
        managed = False
        db_table = 'CNH'


class Capacitando(models.Model):

    idcapacitando = models.IntegerField(db_column='idCapacitando')
    matricula = models.IntegerField(unique=True)

    identificacaosocial = models.BigIntegerField(
        db_column='identificacaoSocial',
        blank=True, null=True)

    responsavelfamilia = models.BooleanField(
        db_column='responsavelFamilia', default=False)
    familia = models.BigIntegerField(blank=True, null=True)

    rendapercapita = models.FloatField(
        db_column='rendaPerCapita', blank=True, null=True)

    atualizacaocadastral = models.DateField(
        db_column='atualizacaoCadastral', blank=True, null=True)

    inicioatividades = models.DateField(
        db_column='inicioAtividades', blank=True, null=True)

    status = models.BooleanField(default=True, blank=True)

    dataregistro = models.DateField(
        db_column='dataRegistro', blank=True, null=True, auto_now=True)

    horaregistro = models.TimeField(
        db_column='horaRegistro', blank=True, null=True, auto_now=True)

    areaatuacao = models.ForeignKey(AreaAtuacao, db_column='AreaAtuacao')

    especialidade = models.ForeignKey(
        'Especialidade', db_column='Especialidade')

    pessoa = models.ForeignKey('Pessoa', db_column='Pessoa')

    necessidadeespecial = models.ForeignKey(
        'NecessidadeEspecial', db_column='NecessidadeEspecial')

    categoria = models.ForeignKey('Categoria', db_column='Categoria')

    unidade = models.ForeignKey('Unidade', db_column='Unidade')

    turno_idturno = models.ForeignKey('Turno', db_column='Turno_idTurno')

    class Meta:
        managed = False
        db_table = 'Capacitando'


class CarteiraTrabalho(models.Model):

    idcarteiratrabalho = models.IntegerField(db_column='idCarteiraTrabalho')
    ctps = models.BigIntegerField(blank=True, null=True)
    serie = models.IntegerField(blank=True, null=True)

    pessoa = models.ForeignKey('Pessoa', db_column='Pessoa')

    class Meta:
        managed = False
        db_table = 'CarteiraTrabalho'


class Categoria(models.Model):

    idcategoria = models.IntegerField(
        db_column='idCategoria', primary_key=True)
    descricao = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'Categoria'


class CategoriaCNH(models.Model):

    idcategoriacnh = models.IntegerField(
        db_column='idCategoriaCNH', primary_key=True)
    categoria = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'CategoriaCNH'


class Cidade(models.Model):

    idcidade = models.IntegerField(db_column='idCidade')
    uf = models.ForeignKey('UF', db_column='UF')
    nome = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'Cidade'


class Desligamento(models.Model):

    iddesligamento = models.IntegerField(db_column='idDesligamento')
    data = models.DateField(blank=True, null=True, auto_now=True)

    capacitando = models.ForeignKey(Capacitando, db_column='Capacitando')

    class Meta:
        managed = False
        db_table = 'Desligamento'


class Email(models.Model):

    idemail = models.IntegerField(db_column='idEmail')
    endereco = models.CharField(max_length=255, blank=True)

    pessoa = models.ForeignKey('Pessoa', db_column='Pessoa')

    class Meta:
        managed = False
        db_table = 'Email'


class Endereco(models.Model):

    idendereco = models.IntegerField(db_column='idEndereco')
    cep = models.BigIntegerField(blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True)
    bairro = models.CharField(max_length=255, blank=True)

    cidade = models.ForeignKey(Cidade, db_column='Cidade')

    class Meta:
        managed = False
        db_table = 'Endereco'


class Especialidade(models.Model):

    idsubarea = models.IntegerField(db_column='idSubArea', primary_key=True)
    descricao = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'Especialidade'


class EstadoCivil(models.Model):

    idestadocivil = models.IntegerField(
        db_column='idEstadoCivil', primary_key=True)
    descricao = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'EstadoCivil'


class Etnia(models.Model):

    idetnia = models.IntegerField(db_column='idEtnia', primary_key=True)
    descricao = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'Etnia'


class Filiacao(models.Model):

    idfiliacao = models.IntegerField(db_column='idFiliacao')
    cpf = models.BigIntegerField(unique=True, blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True)

    pessoa = models.ForeignKey('Pessoa', db_column='Pessoa')

    class Meta:
        managed = False
        db_table = 'Filiacao'


class Nacionalidade(models.Model):

    idnacionalidade = models.IntegerField(
        db_column='idNacionalidade', primary_key=True)
    descricao = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'Nacionalidade'


class Pais(models.Model):

    idpais = models.IntegerField(db_column='idPais', primary_key=True)
    nome = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'Pais'


class UF(models.Model):
    iduf = models.IntegerField(db_column='idUF')

    pais = models.ForeignKey(Pais, db_column='Pais')
    abreviacao = models.CharField(max_length=2, blank=True)
    nome = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'UF'


class Naturalidade(models.Model):

    idnaturalidade = models.IntegerField(db_column='idNaturalidade')

    pais = models.ForeignKey('Pais', db_column='Pais')

    cidade = models.ForeignKey(Cidade, db_column='Cidade')
    uf = models.ForeignKey(UF, db_column='UF')

    class Meta:
        managed = False
        db_table = 'Naturalidade'


class NecessidadeEspecial(models.Model):

    idnecessidadeespecial = models.IntegerField(
        db_column='idNecessidadeEspecial', primary_key=True)
    descricao = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'NecessidadeEspecial'


class Pessoa(models.Model):

    idpessoa = models.IntegerField(db_column='idPessoa')
    cpf = models.BigIntegerField(unique=True)
    nome = models.CharField(max_length=255, blank=True)

    datanascimento = models.DateField(
        db_column='dataNascimento', blank=True, null=True)
    sexo = models.BooleanField(default=False)
    filhos = models.BooleanField(default=False)
    foto = models.CharField(max_length=255, blank=True)

    etnia = models.ForeignKey(Etnia, db_column='Etnia')

    tipoidentidade = models.ForeignKey(
        'TipoIdentidade', db_column='TipoIdentidade')

    estadocivil = models.ForeignKey(EstadoCivil, db_column='EstadoCivil')

    endereco = models.ForeignKey(Endereco, db_column='Endereco')

    naturalidade = models.ForeignKey(Naturalidade, db_column='Naturalidade')

    class Meta:
        managed = False
        db_table = 'Pessoa'


class Ponto(models.Model):

    idponto = models.IntegerField(db_column='idPonto')
    data = models.DateField(blank=True, null=True, auto_now=True)
    hora = models.TimeField(blank=True, null=True, auto_now=True)

    pessoa = models.ForeignKey(Pessoa, db_column='Pessoa')

    tipoponto = models.ForeignKey('TipoPonto', db_column='TipoPonto')

    class Meta:
        managed = False
        db_table = 'Ponto'


class RegistroGeral(models.Model):

    idregistrogeral = models.IntegerField(db_column='idRegistroGeral')
    rg = models.BigIntegerField(unique=True, blank=True, null=True)

    orgaoexpedidor = models.CharField(
        db_column='orgaoExpedidor', max_length=45, blank=True)

    dataexpedicao = models.DateField(
        db_column='dataExpedicao', blank=True, null=True)

    pessoa = models.ForeignKey(Pessoa, db_column='Pessoa')
    uf = models.ForeignKey('UF', db_column='UF')

    class Meta:
        managed = False
        db_table = 'RegistroGeral'


class Reservista(models.Model):

    idreservista = models.IntegerField(db_column='idReservista')
    certificado = models.BigIntegerField(blank=True, null=True)
    serie = models.BigIntegerField(blank=True, null=True)
    orgao = models.CharField(max_length=255, blank=True)

    dispensaincorporacao = models.BigIntegerField(
        db_column='dispensaIncorporacao', blank=True, null=True)

    unidadealistamento = models.CharField(
        db_column='unidadeAlistamento', max_length=255, blank=True)

    pessoa = models.ForeignKey(Pessoa, db_column='Pessoa')

    class Meta:
        managed = False
        db_table = 'Reservista'


class ServicoMilitar(models.Model):

    idservicomilitar = models.IntegerField(db_column='idServicoMilitar')
    ano = models.IntegerField(blank=True, null=True)

    pessoa = models.ForeignKey(Pessoa, db_column='Pessoa')
    uf = models.ForeignKey('UF', db_column='UF')

    class Meta:
        managed = False
        db_table = 'ServicoMilitar'


class Telefone(models.Model):

    idtelefone = models.IntegerField(db_column='idTelefone')
    numero = models.CharField(max_length=255, blank=True)

    tipotelefone = models.ForeignKey('TipoTelefone', db_column='TipoTelefone')

    pessoa = models.ForeignKey(Pessoa, db_column='Pessoa')

    class Meta:
        managed = False
        db_table = 'Telefone'


class TipoIdentidade(models.Model):

    idtipoidentidade = models.IntegerField(
        db_column='idTipoIdentidade', primary_key=True)
    descricao = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'TipoIdentidade'


class TipoPonto(models.Model):

    idtipoponto = models.IntegerField(
        db_column='idTipoPonto', primary_key=True)
    descricao = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'TipoPonto'


class TipoTelefone(models.Model):

    idtipotelefone = models.IntegerField(
        db_column='idTipoTelefone', primary_key=True)
    descricao = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'TipoTelefone'


class TituloEleitor(models.Model):

    idtituloeleitor = models.IntegerField(db_column='idTituloEleitor')
    titulo = models.BigIntegerField(blank=True, null=True)
    zona = models.IntegerField(blank=True, null=True)
    secao = models.IntegerField(blank=True, null=True)

    pessoa = models.ForeignKey(Pessoa, db_column='Pessoa')

    cidade = models.ForeignKey(Cidade, db_column='Cidade')

    class Meta:
        managed = False
        db_table = 'TituloEleitor'


class Turno(models.Model):

    idturno = models.IntegerField(db_column='idTurno', primary_key=True)
    descricao = models.CharField(max_length=255, blank=True)
    entrada = models.TimeField(blank=True, null=True, auto_now=True)

    saidalanche = models.TimeField(
        db_column='saidaLanche', blank=True, null=True, auto_now=True)

    entradalanche = models.TimeField(
        db_column='entradaLanche', blank=True, null=True, auto_now=True)
    saida = models.TimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'Turno'


class Unidade(models.Model):

    idunidade = models.IntegerField(db_column='idUnidade')

    cidade = models.ForeignKey(Cidade, db_column='Cidade')

    class Meta:
        managed = False
        db_table = 'Unidade'
