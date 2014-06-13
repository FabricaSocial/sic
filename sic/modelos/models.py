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

class Areaatuacao(models.Model):
    idareaatuacao = models.IntegerField(db_column='idAreaAtuacao', primary_key=True) # Field name made lowercase.
    nome = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'AreaAtuacao'

class Cnh(models.Model):
    idcnh = models.IntegerField(db_column='idCNH') # Field name made lowercase.
    numero = models.BigIntegerField()
    dataemissao = models.DateField(db_column='dataEmissao', blank=True, null=True) # Field name made lowercase.
    validade = models.DateField(blank=True, null=True)
    uf = models.ForeignKey('Uf', db_column='UF') # Field name made lowercase.
    categoriacnh = models.ForeignKey('Categoriacnh', db_column='CategoriaCNH') # Field name made lowercase.
    pessoa = models.ForeignKey('Pessoa', db_column='Pessoa') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'CNH'

class Capacitando(models.Model):
    idcapacitando = models.IntegerField(db_column='idCapacitando') # Field name made lowercase.
    matricula = models.IntegerField(unique=True)
    identificacaosocial = models.BigIntegerField(db_column='identificacaoSocial', blank=True, null=True) # Field name made lowercase.
    responsavelfamilia = models.CharField(db_column='responsavelFamilia', max_length=1, blank=True) # Field name made lowercase.
    familia = models.BigIntegerField(blank=True, null=True)
    rendapercapita = models.FloatField(db_column='rendaPerCapita', blank=True, null=True) # Field name made lowercase.
    atualizacaocadastral = models.DateField(db_column='atualizacaoCadastral', blank=True, null=True) # Field name made lowercase.
    inicioatividades = models.DateField(db_column='inicioAtividades', blank=True, null=True) # Field name made lowercase.
    status = models.CharField(max_length=1, blank=True)
    dataregistro = models.DateField(db_column='dataRegistro', blank=True, null=True, auto_now=True) # Field name made lowercase.
    horaregistro = models.TimeField(db_column='horaRegistro', blank=True, null=True, auto_now=True) # Field name made lowercase.
    areaatuacao = models.ForeignKey(Areaatuacao, db_column='AreaAtuacao') # Field name made lowercase.
    especialidade = models.ForeignKey('Especialidade', db_column='Especialidade') # Field name made lowercase.
    pessoa = models.ForeignKey('Pessoa', db_column='Pessoa') # Field name made lowercase.
    necessidadeespecial = models.ForeignKey('Necessidadeespecial', db_column='NecessidadeEspecial') # Field name made lowercase.
    categoria = models.ForeignKey('Categoria', db_column='Categoria') # Field name made lowercase.
    unidade = models.ForeignKey('Unidade', db_column='Unidade') # Field name made lowercase.
    turno_idturno = models.ForeignKey('Turno', db_column='Turno_idTurno') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Capacitando'

class Carteiratrabalho(models.Model):
    idcarteiratrabalho = models.IntegerField(db_column='idCarteiraTrabalho') # Field name made lowercase.
    ctps = models.BigIntegerField(blank=True, null=True)
    serie = models.IntegerField(blank=True, null=True)
    pessoa = models.ForeignKey('Pessoa', db_column='Pessoa') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'CarteiraTrabalho'

class Categoria(models.Model):
    idcategoria = models.IntegerField(db_column='idCategoria', primary_key=True) # Field name made lowercase.
    descricao = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'Categoria'

class Categoriacnh(models.Model):
    idcategoriacnh = models.IntegerField(db_column='idCategoriaCNH', primary_key=True) # Field name made lowercase.
    categoria = models.CharField(max_length=45, blank=True)
    class Meta:
        managed = False
        db_table = 'CategoriaCNH'

class Cidade(models.Model):
    idcidade = models.IntegerField(db_column='idCidade') # Field name made lowercase.
    uf = models.ForeignKey('Uf', db_column='UF') # Field name made lowercase.
    nome = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'Cidade'

class Desligamento(models.Model):
    iddesligamento = models.IntegerField(db_column='idDesligamento') # Field name made lowercase.
    data = models.DateField(blank=True, null=True, auto_now=True)
    capacitando = models.ForeignKey(Capacitando, db_column='Capacitando') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Desligamento'

class Email(models.Model):
    idemail = models.IntegerField(db_column='idEmail') # Field name made lowercase.
    endereco = models.CharField(max_length=255, blank=True)
    pessoa = models.ForeignKey('Pessoa', db_column='Pessoa') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Email'

class Endereco(models.Model):
    idendereco = models.IntegerField(db_column='idEndereco') # Field name made lowercase.
    cep = models.BigIntegerField(blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True)
    bairro = models.CharField(max_length=255, blank=True)
    cidade = models.ForeignKey(Cidade, db_column='Cidade') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Endereco'

class Especialidade(models.Model):
    idsubarea = models.IntegerField(db_column='idSubArea', primary_key=True) # Field name made lowercase.
    descricao = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'Especialidade'

class Estadocivil(models.Model):
    idestadocivil = models.IntegerField(db_column='idEstadoCivil', primary_key=True) # Field name made lowercase.
    descricao = models.CharField(max_length=45, blank=True)
    class Meta:
        managed = False
        db_table = 'EstadoCivil'

class Etnia(models.Model):
    idetnia = models.IntegerField(db_column='idEtnia', primary_key=True) # Field name made lowercase.
    descricao = models.CharField(max_length=45, blank=True)
    class Meta:
        managed = False
        db_table = 'Etnia'

class Filiacao(models.Model):
    idfiliacao = models.IntegerField(db_column='idFiliacao') # Field name made lowercase.
    cpf = models.BigIntegerField(unique=True, blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True)
    pessoa = models.ForeignKey('Pessoa', db_column='Pessoa') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Filiacao'

class Nacionalidade(models.Model):
    idnacionalidade = models.IntegerField(db_column='idNacionalidade', primary_key=True) # Field name made lowercase.
    descricao = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'Nacionalidade'

class Naturalidade(models.Model):
    idnaturalidade = models.IntegerField(db_column='idNaturalidade') # Field name made lowercase.
    pais = models.ForeignKey('Pais', db_column='Pais') # Field name made lowercase.
    cidade = models.ForeignKey(Cidade, db_column='Cidade') # Field name made lowercase.
    uf = models.ForeignKey(Cidade, db_column='UF') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Naturalidade'

class Necessidadeespecial(models.Model):
    idnecessidadeespecial = models.IntegerField(db_column='idNecessidadeEspecial', primary_key=True) # Field name made lowercase.
    descricao = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'NecessidadeEspecial'

class Pais(models.Model):
    idpais = models.IntegerField(db_column='idPais', primary_key=True) # Field name made lowercase.
    nome = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'Pais'

class Pessoa(models.Model):
    idpessoa = models.IntegerField(db_column='idPessoa') # Field name made lowercase.
    cpf = models.BigIntegerField(unique=True)
    nome = models.CharField(max_length=255, blank=True)
    datanascimento = models.DateField(db_column='dataNascimento', blank=True, null=True) # Field name made lowercase.
    sexo = models.CharField(max_length=1, blank=True)
    filhos = models.CharField(max_length=1, blank=True)
    foto = models.CharField(max_length=255, blank=True)
    etnia = models.ForeignKey(Etnia, db_column='Etnia') # Field name made lowercase.
    tipoidentidade = models.ForeignKey('Tipoidentidade', db_column='TipoIdentidade') # Field name made lowercase.
    estadocivil = models.ForeignKey(Estadocivil, db_column='EstadoCivil') # Field name made lowercase.
    endereco = models.ForeignKey(Endereco, db_column='Endereco') # Field name made lowercase.
    naturalidade = models.ForeignKey(Naturalidade, db_column='Naturalidade') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Pessoa'

class Ponto(models.Model):
    idponto = models.IntegerField(db_column='idPonto') # Field name made lowercase.
    data = models.DateField(blank=True, null=True, auto_now=True)
    hora = models.TimeField(blank=True, null=True, auto_now=True)
    pessoa = models.ForeignKey(Pessoa, db_column='Pessoa') # Field name made lowercase.
    tipoponto = models.ForeignKey('Tipoponto', db_column='TipoPonto') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Ponto'

class Registrogeral(models.Model):
    idregistrogeral = models.IntegerField(db_column='idRegistroGeral') # Field name made lowercase.
    rg = models.BigIntegerField(unique=True, blank=True, null=True)
    orgaoexpedidor = models.CharField(db_column='orgaoExpedidor', max_length=45, blank=True) # Field name made lowercase.
    dataexpedicao = models.DateField(db_column='dataExpedicao', blank=True, null=True) # Field name made lowercase.
    pessoa = models.ForeignKey(Pessoa, db_column='Pessoa') # Field name made lowercase.
    uf = models.ForeignKey('Uf', db_column='UF') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'RegistroGeral'

class Reservista(models.Model):
    idreservista = models.IntegerField(db_column='idReservista') # Field name made lowercase.
    certificado = models.BigIntegerField(blank=True, null=True)
    serie = models.BigIntegerField(blank=True, null=True)
    orgao = models.CharField(max_length=255, blank=True)
    dispensaincorporacao = models.BigIntegerField(db_column='dispensaIncorporacao', blank=True, null=True) # Field name made lowercase.
    unidadealistamento = models.CharField(db_column='unidadeAlistamento', max_length=255, blank=True) # Field name made lowercase.
    pessoa = models.ForeignKey(Pessoa, db_column='Pessoa') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Reservista'

class Servicomilitar(models.Model):
    idservicomilitar = models.IntegerField(db_column='idServicoMilitar') # Field name made lowercase.
    ano = models.IntegerField(blank=True, null=True)
    pessoa = models.ForeignKey(Pessoa, db_column='Pessoa') # Field name made lowercase.
    uf = models.ForeignKey('Uf', db_column='UF') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ServicoMilitar'

class Telefone(models.Model):
    idtelefone = models.IntegerField(db_column='idTelefone') # Field name made lowercase.
    numero = models.CharField(max_length=255, blank=True)
    tipotelefone = models.ForeignKey('Tipotelefone', db_column='TipoTelefone') # Field name made lowercase.
    pessoa = models.ForeignKey(Pessoa, db_column='Pessoa') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Telefone'

class Tipoidentidade(models.Model):
    idtipoidentidade = models.IntegerField(db_column='idTipoIdentidade', primary_key=True) # Field name made lowercase.
    descricao = models.CharField(max_length=45, blank=True)
    class Meta:
        managed = False
        db_table = 'TipoIdentidade'

class Tipoponto(models.Model):
    idtipoponto = models.IntegerField(db_column='idTipoPonto', primary_key=True) # Field name made lowercase.
    descricao = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'TipoPonto'

class Tipotelefone(models.Model):
    idtipotelefone = models.IntegerField(db_column='idTipoTelefone', primary_key=True) # Field name made lowercase.
    descricao = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'TipoTelefone'

class Tituloeleitor(models.Model):
    idtituloeleitor = models.IntegerField(db_column='idTituloEleitor') # Field name made lowercase.
    titulo = models.BigIntegerField(blank=True, null=True)
    zona = models.IntegerField(blank=True, null=True)
    secao = models.IntegerField(blank=True, null=True)
    pessoa = models.ForeignKey(Pessoa, db_column='Pessoa') # Field name made lowercase.
    cidade = models.ForeignKey(Cidade, db_column='Cidade') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'TituloEleitor'

class Turno(models.Model):
    idturno = models.IntegerField(db_column='idTurno', primary_key=True) # Field name made lowercase.
    descricao = models.CharField(max_length=255, blank=True)
    entrada = models.TimeField(blank=True, null=True, auto_now=True)
    saidalanche = models.TimeField(db_column='saidaLanche', blank=True, null=True, auto_now=True) # Field name made lowercase.
    entradalanche = models.TimeField(db_column='entradaLanche', blank=True, null=True, auto_now=True) # Field name made lowercase.
    saida = models.TimeField(blank=True, null=True, auto_now=True)
    class Meta:
        managed = False
        db_table = 'Turno'

class Uf(models.Model):
    iduf = models.IntegerField(db_column='idUF') # Field name made lowercase.
    pais = models.ForeignKey(Pais, db_column='Pais') # Field name made lowercase.
    abreviacao = models.CharField(max_length=2, blank=True)
    nome = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'UF'

class Unidade(models.Model):
    idunidade = models.IntegerField(db_column='idUnidade') # Field name made lowercase.
    cidade = models.ForeignKey(Cidade, db_column='Cidade') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Unidade'

