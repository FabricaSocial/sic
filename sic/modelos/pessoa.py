from django.db import models


class CategoriaCNH(models.Model):

    class Meta:
        db_table = 'CategoriaCNH'

    def __unicode__(self):
        return self.categoria

    categoria = models.CharField(max_length=255)


class Nacionalidade(models.Model):

    class Meta:
        db_table = 'Nacionalidade'

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255)


class TipoIdentidade(models.Model):

    class Meta:
        db_table = 'TipoIdentidade'

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255)


class TipoTelefone(models.Model):

    class Meta:
        db_table = 'TipoTelefone'

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255)


class Pais(models.Model):

    class Meta:
        db_table = 'Pais'

    def __unicode__(self):
        return self.nome

    nome = models.CharField(max_length=255)


class Etnia(models.Model):

    class Meta:
        db_table = 'Etnia'

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255)


class UF(models.Model):

    class Meta:
        db_table = 'UF'

    def __unicode__(self):
        return self.abreviacao

    pais = models.ForeignKey(Pais)
    abreviacao = models.CharField(max_length=2)
    nome = models.CharField(max_length=255)


class Cidade(models.Model):

    class Meta:
        db_table = 'Cidade'

    def __unicode__(self):
        return self.nome

    uf = models.ForeignKey(UF)
    nome = models.CharField(max_length=255)


class Naturalidade(models.Model):

    class Meta:
        db_table = 'Naturalidade'

    def __unicode__(self):
        return self.cidade.nome

    pais = models.ForeignKey(Pais)
    cidade = models.ForeignKey(Cidade, null=True)
    uf = models.ForeignKey(UF, null=True)


class Endereco(models.Model):

    class Meta:
        db_table = 'Endereco'

    def __unicode__(self):
        return self.endereco

    cep = models.BigIntegerField()
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.ForeignKey(Cidade)


class EstadoCivil(models.Model):

    class Meta:
        db_table = 'EstadoCivil'

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255)


class Pessoa(models.Model):

    class Meta:
        db_table = 'Pessoa'

    def __unicode__(self):
        self.nome

    cpf = models.BigIntegerField()
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    sexo = models.BooleanField()
    filhos = models.BooleanField()
    foto = models.CharField(max_length=255, null=True)
    etnia = models.ForeignKey(Etnia)
    tipo_identidade = models.ForeignKey(TipoIdentidade)
    estado_civil = models.ForeignKey(EstadoCivil)
    endereco = models.ForeignKey(Endereco)
    nacionalidade = models.ForeignKey(Nacionalidade)
    naturalidade = models.ForeignKey(Naturalidade)


class Reservista(models.Model):

    class Meta:
        db_table = 'Reservista'

    def __unicode__(self):
        self.certificado

    certificado = models.BigIntegerField()
    serie = models.BigIntegerField()
    orgao = models.CharField(max_length=255)
    dispensa_incorporacao = models.BigIntegerField()
    unidade_alistamento = models.CharField(max_length=255)
    pessoa = models.ForeignKey(Pessoa)


class RegistroGeral(models.Model):

    class Meta:
        db_table = 'RegistroGeral'

    def __unicode__(self):
        self.rg

    rg = models.BigIntegerField()
    orgao_expedidor = models.CharField(max_length=255)
    data_expedicao = models.DateField()
    pessoa = models.ForeignKey(Pessoa)
    uf = models.ForeignKey(UF)


class ServicoMilitar(models.Model):

    class Meta:
        db_table = 'ServicoMilitar'

    def __unicode__(self):
        self.pessoa.nome

    ano = models.IntegerField()
    pessoa = models.ForeignKey(Pessoa)
    uf = models.ForeignKey(UF)


class CarteiraTrabalho(models.Model):

    class Meta:
        db_table = 'CarteiraTrabalho'

    def __unicode__(self):
        self.pessoa.nome

    ctps = models.BigIntegerField()
    serie = models.IntegerField()
    pessoa = models.ForeignKey(Pessoa)


class Filiacao(models.Model):

    class Meta:
        db_table = 'Filiacao'

    def __unicode__(self):
        self.nome

    cpf = models.BigIntegerField()
    nome = models.CharField(max_length=255)
    pessoa = models.ForeignKey(Pessoa)


class CNH(models.Model):

    class Meta:
        db_table = 'CNH'

    def __unicode__(self):
        self.numero

    numero = models.BigIntegerField()
    data_emissao = models.DateField()
    validade = models.DateField()
    uf = models.ForeignKey(UF)
    categoria_cnh = models.ForeignKey(CategoriaCNH)
    pessoa = models.ForeignKey(Pessoa)


class Telefone(models.Model):

    class Meta:
        db_table = 'Telefone'

    def __unicode__(self):
        self.numero

    numero = models.BigIntegerField()
    tipo_telefone = models.ForeignKey(TipoTelefone)
    pessoa = models.ForeignKey(Pessoa)


class Email(models.Model):

    class Meta:
        db_table = 'Email'

    def __unicode__(self):
        self.endereco

    endereco = models.CharField(max_length=255)
    pessoa = models.ForeignKey(Pessoa)


class TituloEleitor(models.Model):

    class Meta:
        db_table = 'TituloEleitor'

    def __unicode__(self):
        self.titulo

    titulo = models.BigIntegerField()
    zona = models.IntegerField()
    secao = models.IntegerField()
    pessoa = models.ForeignKey(Pessoa)
    cidade = models.ForeignKey(Cidade)
