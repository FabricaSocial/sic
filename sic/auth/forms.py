# -*- coding: utf-8 -*-

from django import forms
from modelos.funcionario import Funcionario
from modelos.pessoa import Pessoa, Endereco, Naturalidade, RegistroGeral, Email


class FuncionarioForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = ['matricula', 'cargo', 'departamento', 'ramal']


class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = ['cpf', 'nome', 'data_nascimento', 'sexo',
                  'filhos', 'estado_civil', 'foto', 'etnia']

    cpf = forms.IntegerField(min_value=0, label='CPF')


class EnderecoForm(forms.ModelForm):

    class Meta:
        model = Endereco
        fields = ['cep', 'endereco', 'bairro', 'cidade']


class NaturalidadeForm(forms.ModelForm):

    class Meta:
        model = Naturalidade
        fields = ['pais', 'cidade', 'uf']


class RegistroGeralForm(forms.ModelForm):

    class Meta:
        model = RegistroGeral
        fields = ['rg', 'orgao_expedidor', 'data_expedicao', 'uf']

    rg = forms.IntegerField(min_value=1, label='RG')
    orgao_expedidor = forms.CharField(label='Órgão Expedidor')
    data_expedicao = forms.DateField(
        input_formats=['%m/%d/%Y'], label='Data de Expedição')


class EmailForm(forms.ModelForm):

    class Meta:
        model = Email
        fields = ['endereco']

    email = forms.EmailField(label='Email')
