# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'TipoEntrada'
        db.delete_table(u'modelos_tipoentrada')


    def backwards(self, orm):
        # Adding model 'TipoEntrada'
        db.create_table(u'modelos_tipoentrada', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'modelos', ['TipoEntrada'])


    models = {
        u'modelos.areaatuacao': {
            'Meta': {'object_name': 'AreaAtuacao', 'db_table': "u'AreaAtuacao'", 'managed': 'False'},
            'idareaatuacao': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'idAreaAtuacao'"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'modelos.capacitando': {
            'Meta': {'object_name': 'Capacitando', 'db_table': "u'Capacitando'", 'managed': 'False'},
            'areaatuacao': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.AreaAtuacao']", 'db_column': "u'AreaAtuacao'"}),
            'atualizacaocadastral': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'atualizacaoCadastral'", 'blank': 'True'}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Categoria']", 'db_column': "u'Categoria'"}),
            'dataregistro': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'db_column': "u'dataRegistro'", 'blank': 'True'}),
            'especialidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Especialidade']", 'db_column': "u'Especialidade'"}),
            'familia': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'horaregistro': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'null': 'True', 'db_column': "u'horaRegistro'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idcapacitando': ('django.db.models.fields.IntegerField', [], {'db_column': "u'idCapacitando'"}),
            'identificacaosocial': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'identificacaoSocial'", 'blank': 'True'}),
            'inicioatividades': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'inicioAtividades'", 'blank': 'True'}),
            'matricula': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'necessidadeespecial': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.NecessidadeEspecial']", 'db_column': "u'NecessidadeEspecial'"}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'db_column': "u'Pessoa'"}),
            'rendapercapita': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'rendaPerCapita'", 'blank': 'True'}),
            'responsavelfamilia': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'responsavelFamilia'"}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'turno_idturno': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Turno']", 'db_column': "u'Turno_idTurno'"}),
            'unidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Unidade']", 'db_column': "u'Unidade'"})
        },
        u'modelos.carteiratrabalho': {
            'Meta': {'object_name': 'CarteiraTrabalho', 'db_table': "u'CarteiraTrabalho'", 'managed': 'False'},
            'ctps': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idcarteiratrabalho': ('django.db.models.fields.IntegerField', [], {'db_column': "u'idCarteiraTrabalho'"}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'db_column': "u'Pessoa'"}),
            'serie': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'modelos.categoria': {
            'Meta': {'object_name': 'Categoria', 'db_table': "u'Categoria'", 'managed': 'False'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'idcategoria': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'idCategoria'"})
        },
        u'modelos.categoriacnh': {
            'Meta': {'object_name': 'CategoriaCNH', 'db_table': "u'CategoriaCNH'", 'managed': 'False'},
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'idcategoriacnh': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'idCategoriaCNH'"})
        },
        u'modelos.cidade': {
            'Meta': {'object_name': 'Cidade', 'db_table': "u'Cidade'", 'managed': 'False'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idcidade': ('django.db.models.fields.IntegerField', [], {'db_column': "u'idCidade'"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.UF']", 'db_column': "u'UF'"})
        },
        u'modelos.cnh': {
            'Meta': {'object_name': 'CNH', 'db_table': "u'CNH'", 'managed': 'False'},
            'categoriacnh': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.CategoriaCNH']", 'db_column': "u'CategoriaCNH'"}),
            'dataemissao': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'dataEmissao'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idcnh': ('django.db.models.fields.IntegerField', [], {'db_column': "u'idCNH'"}),
            'numero': ('django.db.models.fields.BigIntegerField', [], {}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'db_column': "u'Pessoa'"}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.UF']", 'db_column': "u'UF'"}),
            'validade': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'modelos.desligamento': {
            'Meta': {'object_name': 'Desligamento', 'db_table': "u'Desligamento'", 'managed': 'False'},
            'capacitando': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Capacitando']", 'db_column': "u'Capacitando'"}),
            'data': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iddesligamento': ('django.db.models.fields.IntegerField', [], {'db_column': "u'idDesligamento'"})
        },
        u'modelos.email': {
            'Meta': {'object_name': 'Email', 'db_table': "u'Email'", 'managed': 'False'},
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idemail': ('django.db.models.fields.IntegerField', [], {'db_column': "u'idEmail'"}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'db_column': "u'Pessoa'"})
        },
        u'modelos.endereco': {
            'Meta': {'object_name': 'Endereco', 'db_table': "u'Endereco'", 'managed': 'False'},
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cep': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Cidade']", 'db_column': "u'Cidade'"}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idendereco': ('django.db.models.fields.IntegerField', [], {'db_column': "u'idEndereco'"})
        },
        u'modelos.especialidade': {
            'Meta': {'object_name': 'Especialidade', 'db_table': "u'Especialidade'", 'managed': 'False'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'idsubarea': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'idSubArea'"})
        },
        u'modelos.estadocivil': {
            'Meta': {'object_name': 'EstadoCivil', 'db_table': "u'EstadoCivil'", 'managed': 'False'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'idestadocivil': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'idEstadoCivil'"})
        },
        u'modelos.etnia': {
            'Meta': {'object_name': 'Etnia', 'db_table': "u'Etnia'", 'managed': 'False'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'idetnia': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'idEtnia'"})
        },
        u'modelos.filiacao': {
            'Meta': {'object_name': 'Filiacao', 'db_table': "u'Filiacao'", 'managed': 'False'},
            'cpf': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idfiliacao': ('django.db.models.fields.IntegerField', [], {'db_column': "u'idFiliacao'"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'db_column': "u'Pessoa'"})
        },
        u'modelos.nacionalidade': {
            'Meta': {'object_name': 'Nacionalidade', 'db_table': "u'Nacionalidade'", 'managed': 'False'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'idnacionalidade': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'idNacionalidade'"})
        },
        u'modelos.naturalidade': {
            'Meta': {'object_name': 'Naturalidade', 'db_table': "u'Naturalidade'", 'managed': 'False'},
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Cidade']", 'db_column': "u'Cidade'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idnaturalidade': ('django.db.models.fields.IntegerField', [], {'db_column': "u'idNaturalidade'"}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pais']", 'db_column': "u'Pais'"}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.UF']", 'db_column': "u'UF'"})
        },
        u'modelos.necessidadeespecial': {
            'Meta': {'object_name': 'NecessidadeEspecial', 'db_table': "u'NecessidadeEspecial'", 'managed': 'False'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'idnecessidadeespecial': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'idNecessidadeEspecial'"})
        },
        u'modelos.pais': {
            'Meta': {'object_name': 'Pais', 'db_table': "u'Pais'", 'managed': 'False'},
            'idpais': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'idPais'"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'modelos.pessoa': {
            'Meta': {'object_name': 'Pessoa', 'db_table': "u'Pessoa'", 'managed': 'False'},
            'cpf': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'datanascimento': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'dataNascimento'", 'blank': 'True'}),
            'endereco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Endereco']", 'db_column': "u'Endereco'"}),
            'estadocivil': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.EstadoCivil']", 'db_column': "u'EstadoCivil'"}),
            'etnia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Etnia']", 'db_column': "u'Etnia'"}),
            'filhos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'foto': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idpessoa': ('django.db.models.fields.IntegerField', [], {'db_column': "u'idPessoa'"}),
            'naturalidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Naturalidade']", 'db_column': "u'Naturalidade'"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tipoidentidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.TipoIdentidade']", 'db_column': "u'TipoIdentidade'"})
        },
        u'modelos.ponto': {
            'Meta': {'object_name': 'Ponto', 'db_table': "u'Ponto'", 'managed': 'False'},
            'data': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'hora': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idponto': ('django.db.models.fields.IntegerField', [], {'db_column': "u'idPonto'"}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'db_column': "u'Pessoa'"}),
            'tipoponto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.TipoPonto']", 'db_column': "u'TipoPonto'"})
        },
        u'modelos.registrogeral': {
            'Meta': {'object_name': 'RegistroGeral', 'db_table': "u'RegistroGeral'", 'managed': 'False'},
            'dataexpedicao': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'dataExpedicao'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idregistrogeral': ('django.db.models.fields.IntegerField', [], {'db_column': "u'idRegistroGeral'"}),
            'orgaoexpedidor': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "u'orgaoExpedidor'", 'blank': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'db_column': "u'Pessoa'"}),
            'rg': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.UF']", 'db_column': "u'UF'"})
        },
        u'modelos.reservista': {
            'Meta': {'object_name': 'Reservista', 'db_table': "u'Reservista'", 'managed': 'False'},
            'certificado': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dispensaincorporacao': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'dispensaIncorporacao'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idreservista': ('django.db.models.fields.IntegerField', [], {'db_column': "u'idReservista'"}),
            'orgao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'db_column': "u'Pessoa'"}),
            'serie': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'unidadealistamento': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'unidadeAlistamento'", 'blank': 'True'})
        },
        u'modelos.servicomilitar': {
            'Meta': {'object_name': 'ServicoMilitar', 'db_table': "u'ServicoMilitar'", 'managed': 'False'},
            'ano': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idservicomilitar': ('django.db.models.fields.IntegerField', [], {'db_column': "u'idServicoMilitar'"}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'db_column': "u'Pessoa'"}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.UF']", 'db_column': "u'UF'"})
        },
        u'modelos.telefone': {
            'Meta': {'object_name': 'Telefone', 'db_table': "u'Telefone'", 'managed': 'False'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idtelefone': ('django.db.models.fields.IntegerField', [], {'db_column': "u'idTelefone'"}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'db_column': "u'Pessoa'"}),
            'tipotelefone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.TipoTelefone']", 'db_column': "u'TipoTelefone'"})
        },
        u'modelos.tipoidentidade': {
            'Meta': {'object_name': 'TipoIdentidade', 'db_table': "u'TipoIdentidade'", 'managed': 'False'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'idtipoidentidade': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'idTipoIdentidade'"})
        },
        u'modelos.tipoponto': {
            'Meta': {'object_name': 'TipoPonto', 'db_table': "u'TipoPonto'", 'managed': 'False'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'idtipoponto': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'idTipoPonto'"})
        },
        u'modelos.tipotelefone': {
            'Meta': {'object_name': 'TipoTelefone', 'db_table': "u'TipoTelefone'", 'managed': 'False'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'idtipotelefone': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'idTipoTelefone'"})
        },
        u'modelos.tituloeleitor': {
            'Meta': {'object_name': 'TituloEleitor', 'db_table': "u'TituloEleitor'", 'managed': 'False'},
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Cidade']", 'db_column': "u'Cidade'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idtituloeleitor': ('django.db.models.fields.IntegerField', [], {'db_column': "u'idTituloEleitor'"}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'db_column': "u'Pessoa'"}),
            'secao': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'zona': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'modelos.turno': {
            'Meta': {'object_name': 'Turno', 'db_table': "u'Turno'", 'managed': 'False'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'entrada': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'entradalanche': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'null': 'True', 'db_column': "u'entradaLanche'", 'blank': 'True'}),
            'idturno': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'idTurno'"}),
            'saida': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'saidalanche': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'null': 'True', 'db_column': "u'saidaLanche'", 'blank': 'True'})
        },
        u'modelos.uf': {
            'Meta': {'object_name': 'UF', 'db_table': "u'UF'", 'managed': 'False'},
            'abreviacao': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iduf': ('django.db.models.fields.IntegerField', [], {'db_column': "u'idUF'"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pais']", 'db_column': "u'Pais'"})
        },
        u'modelos.unidade': {
            'Meta': {'object_name': 'Unidade', 'db_table': "u'Unidade'", 'managed': 'False'},
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Cidade']", 'db_column': "u'Cidade'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idunidade': ('django.db.models.fields.IntegerField', [], {'db_column': "u'idUnidade'"})
        }
    }

    complete_apps = ['modelos']