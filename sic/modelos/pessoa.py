from django import models


class CategoriaCNH(models.Model):
    categoria = models.CharField(max_length=255)

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


class TipoTelefone(models.Model):
    descricao = models.CharField(max_length=255)

    class Meta:
        db_table = 'TipoTelefone'


class Pais(models.Model):
    nome = models.CharField(max_length=255)

    class Meta:
        db_table = 'Pais'


class Etnia(models.Model):
    descricao = models.CharField(max_length=255)

    class Meta:
        db_table = 'Etnia'


class UF(models.Model):
    pais = models.ForeignKey(Pais)
    abreviacao = models.CharField(max_length=2)
    nome = models.CharField(max_length=255)

    class Meta:
        db_table = 'UF'


class Cidade(models.Model):
    uf = models.ForeignKey(UF)
    nome = models.CharField(max_length=255)

    class Meta:
        db_table = 'Cidade'


class Naturalidade(models.Model):
    pais = models.ForeignKey(Pais)
    cidade = models.ForeignKey(Cidade)
    uf = models.ForeignKey(UF)

    class Meta:
        db_table = 'Naturalidade'


class Endereco(models.Model):
    cep = models.BigIntegerField()
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.ForeignKey(Cidade)

    class Meta:
        db_table = 'Endereco'


class EstadoCivil(models.Model):
    descricao = models.CharField(max_length=255)

    class Meta:
        db_table = 'EstadoCivil'


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
    foto = models.CharField(max_length=255)
    etnia = models.ForeignKey(Etnia)
    tipo_identidade = models.ForeignKey(TipoIdentidade)
    estado_civil = models.ForeignKey(EstadoCivil)
    endereco = models.ForeignKey(Endereco)
    nacionalidade = models.ForeignKey(Nacionalidade)
    naturalidade = models.ForeignKey(Naturalidade)


class Reservista(models.Model):
    certificado = models.BigIntegerField()
    serie = models.BigIntegerField()
    orgao = models.CharField(max_length=255)
    dispensa_incorporacao = models.BigIntegerField()
    unidade_alistamento = models.CharField(max_length=255)
    pessoa = models.ForeignKey(Pessoa)

    class Meta:
        db_table = 'Reservista'


class RegistroGeral(models.Model):
    rg = models.BigIntegerField()
    orgao_expedidor = models.CharField(max_length=255)
    data_expedicao = models.DateField()
    pessoa = models.ForeignKey(Pessoa)
    uf = models.ForeignKey(UF)

    class Meta:
        db_table = 'RegistroGeral'


class ServicoMilitar(models.Model):
    ano = models.IntegerField()
    pessoa = models.ForeignKey(Pessoa)
    uf = models.ForeignKey(UF)

    class Meta:
        db_table = 'ServicoMilitar'


class CarteiraTrabalho(models.Model):
    ctps = models.BigIntegerField()
    serie = models.IntegerField()
    pessoa = models.ForeignKey(Pessoa)

    class Meta:
        db_table = 'CarteiraTrabalho'


class Filiacao(models.Model):
    cpf = models.BigIntegerField()
    nome = models.CharField(max_length=255)
    pessoa = models.ForeignKey(Pessoa)

    class Meta:
        db_table = 'Filiacao'


class CNH(models.Model):
    numero = models.BigIntegerField()
    data_emissao = models.DateField()
    validade = models.DateField()
    uf = models.ForeignKey(UF)
    categoria_cnh = models.ForeignKey(CategoriaCNH)
    pessoa = models.ForeignKey(Pessoa)

    class Meta:
        db_table = 'CNH'


class Telefone(models.Model):
    numero = models.BigIntegerField()
    tipo_telefone = models.ForeignKey(TipoTelefone)
    pessoa = models.ForeignKey(Pessoa)

    class Meta:
        db_table = 'Telefone'


class Email(models.Model):
    endereco = models.CharField(max_length=255)
    pessoa = models.ForeignKey(Pessoa)

    class Meta:
        db_table = 'Email'


class TituloEleitor(models.Model):
    titulo = models.BigIntegerField()
    zona = models.IntegerField()
    secao = models.IntegerField()
    pessoa = models.ForeignKey(Pessoa)
    cidade = models.ForeignKey(Cidade)

    class Meta:
        db_table = 'TituloEleitor'
