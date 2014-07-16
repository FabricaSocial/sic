from django.db import models
from sic.settings import BASE_DIR
from os import path


class CategoriaCNH(models.Model):

    class Meta:
        db_table = 'CategoriaCNH'

    def __unicode__(self):
        return self.categoria

    categoria = models.CharField(max_length=255, null=True)


class Nacionalidade(models.Model):

    class Meta:
        db_table = 'Nacionalidade'

    def natural_key(self):
        return dict(id=self.id, descricao=self.descricao)

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255, null=True)


class TipoIdentidade(models.Model):

    class Meta:
        db_table = 'TipoIdentidade'

    def natural_key(self):
        return dict(id=self.id, descricao=self.descricao)

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255, null=True)


class TipoTelefone(models.Model):

    class Meta:
        db_table = 'TipoTelefone'

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255, null=True)


class Pais(models.Model):

    class Meta:
        db_table = 'Pais'

    def natural_key(self):
        return dict(id=self.id, nome=self.nome)

    def __unicode__(self):
        return self.nome

    nome = models.CharField(max_length=255, null=True)


class Etnia(models.Model):

    class Meta:
        db_table = 'Etnia'

    def natural_key(self):
        return dict(id=self.id, descricao=self.descricao)

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255, null=True)


class UF(models.Model):

    class Meta:
        db_table = 'UF'

    def natural_key(self):
        return dict(id=self.id, pais=self.pais.natural_key(),
                    abreviacao=self.abreviacao, nome=self.nome)

    def __unicode__(self):
        return self.abreviacao

    pais = models.ForeignKey(Pais, null=True)
    abreviacao = models.CharField(max_length=2, null=True)
    nome = models.CharField(max_length=255, null=True)


class Cidade(models.Model):

    class Meta:
        db_table = 'Cidade'

    def natural_key(self):
        return dict(id=self.id, uf=self.uf.natural_key(),
                    nome=self.nome)

    def __unicode__(self):
        return self.nome

    uf = models.ForeignKey(UF, null=True)
    nome = models.CharField(max_length=255, null=True)


class Naturalidade(models.Model):

    class Meta:
        db_table = 'Naturalidade'

    def natural_key(self):
        return dict(id=self.id,
                    pais=self.pais.natural_key(),
                    cidade=self.cidade.natural_key(),
                    uf=self.uf.natural_key())

    def __unicode__(self):
        return self.cidade.nome

    pais = models.ForeignKey(Pais, null=True)
    cidade = models.ForeignKey(Cidade, null=True)
    uf = models.ForeignKey(UF, null=True)


class Endereco(models.Model):

    class Meta:
        db_table = 'Endereco'

    def natural_key(self):
        return dict(id=self.id, cep=self.cep,
                    endereco=self.endereco, bairro=self.bairro,
                    cidade=self.cidade.natural_key())

    def __unicode__(self):
        return self.endereco

    cep = models.BigIntegerField(null=True)
    endereco = models.CharField(max_length=255, null=True)
    bairro = models.CharField(max_length=255, null=True)
    cidade = models.ForeignKey(Cidade, null=True)


class EstadoCivil(models.Model):

    class Meta:
        db_table = 'EstadoCivil'

    def natural_key(self):
        return dict(id=self.id, descricao=self.descricao)

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255, null=True)


class Sexo(models.Model):

    class Meta:
        db_table = 'Sexo'

    def natural_key(self):
        return dict(id=self.id, descricao=self.descricao)

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255, null=True)


class Pessoa(models.Model):

    class Meta:
        db_table = 'Pessoa'

    def natural_key(self):
        return dict(id=self.id, cpf=self.cpf, nome=self.nome,
                    data_nascimento=self.data_nascimento,
                    sexo=self.sexo.natural_key(), filhos=self.filhos,
                    foto=self.foto, etnia=self.etnia.natural_key(),
                    tipo_identidade=self.tipo_identidade.natural_key(),
                    estado_civil=self.estado_civil.natural_key(),
                    endereco=self.endereco.natural_key(),
                    nacionalidade=self.nacionalidade.natural_key(),
                    naturalidade=self.naturalidade.natural_key())

    def __unicode__(self):
        return self.nome

    cpf = models.CharField(max_length=255, null=True)
    nome = models.CharField(max_length=255, null=True)
    data_nascimento = models.DateField(null=True)
    sexo = models.ForeignKey(Sexo, null=True)
    filhos = models.BooleanField(default=False)
    foto = models.ImageField(upload_to=path.join(BASE_DIR, 'static/img/fotos'),
                             null=True)
    etnia = models.ForeignKey(Etnia, null=True)
    tipo_identidade = models.ForeignKey(TipoIdentidade, null=True)
    estado_civil = models.ForeignKey(EstadoCivil, null=True)
    endereco = models.ForeignKey(Endereco, null=True)
    nacionalidade = models.ForeignKey(Nacionalidade, null=True)
    naturalidade = models.ForeignKey(Naturalidade, null=True)


class Reservista(models.Model):

    class Meta:
        db_table = 'Reservista'

    def __unicode__(self):
        self.certificado

    certificado = models.BigIntegerField(null=True)
    serie = models.BigIntegerField(null=True)
    orgao = models.CharField(max_length=255, null=True)
    dispensa_incorporacao = models.BigIntegerField(null=True)
    unidade_alistamento = models.CharField(max_length=255, null=True)
    pessoa = models.ForeignKey(Pessoa, null=True)


class RegistroGeral(models.Model):

    class Meta:
        db_table = 'RegistroGeral'

    def __unicode__(self):
        return str(self.rg)

    rg = models.BigIntegerField(null=True)
    orgao_expedidor = models.CharField(max_length=255, null=True)
    data_expedicao = models.DateField(null=True)
    pessoa = models.ForeignKey(Pessoa, null=True)
    uf = models.ForeignKey(UF, null=True)


class ServicoMilitar(models.Model):

    class Meta:
        db_table = 'ServicoMilitar'

    def __unicode__(self):
        return self.pessoa.nome

    ano = models.IntegerField(null=True)
    pessoa = models.ForeignKey(Pessoa, null=True)
    uf = models.ForeignKey(UF, null=True)


class CarteiraTrabalho(models.Model):

    class Meta:
        db_table = 'CarteiraTrabalho'

    def __unicode__(self):
        return self.pessoa.nome

    ctps = models.BigIntegerField(null=True)
    serie = models.IntegerField(null=True)
    pessoa = models.ForeignKey(Pessoa, null=True)


class Filiacao(models.Model):

    class Meta:
        db_table = 'Filiacao'

    def __unicode__(self):
        return self.nome

    cpf = models.BigIntegerField(null=True)
    nome = models.CharField(max_length=255, null=True)
    pessoa = models.ForeignKey(Pessoa, null=True)


class CNH(models.Model):

    class Meta:
        db_table = 'CNH'

    def __unicode__(self):
        return self.numero

    numero = models.BigIntegerField(null=True)
    data_emissao = models.DateField(null=True)
    validade = models.DateField(null=True)
    uf = models.ForeignKey(UF, null=True)
    categoria_cnh = models.ForeignKey(CategoriaCNH, null=True)
    pessoa = models.ForeignKey(Pessoa, null=True)


class Telefone(models.Model):

    class Meta:
        db_table = 'Telefone'

    def __unicode__(self):
        return self.numero

    numero = models.BigIntegerField(null=True)
    tipo_telefone = models.ForeignKey(TipoTelefone, null=True)
    pessoa = models.ForeignKey(Pessoa, null=True)


class Email(models.Model):

    class Meta:
        db_table = 'Email'

    def __unicode__(self):
        return str(self.endereco)

    endereco = models.CharField(max_length=255, null=True)
    pessoa = models.ForeignKey(Pessoa, null=True)


class TituloEleitor(models.Model):

    class Meta:
        db_table = 'TituloEleitor'

    def __unicode__(self):
        return self.titulo

    titulo = models.BigIntegerField(null=True)
    zona = models.IntegerField(null=True)
    secao = models.IntegerField(null=True)
    pessoa = models.ForeignKey(Pessoa, null=True)
    cidade = models.ForeignKey(Cidade, null=True)
