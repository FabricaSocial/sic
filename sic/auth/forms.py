# -*- coding: utf-8 -*-

from django import forms
from modelos.funcionario import Funcionario
from modelos.pessoa import Pessoa, Endereco, Naturalidade, RegistroGeral, Email


class FuncionarioForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = ['id', 'matricula', 'cargo', 'departamento', 'ramal']


class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = ['id', 'cpf', 'nome', 'data_nascimento', 'sexo',
                  'filhos', 'estado_civil', 'foto', 'etnia']

        foto = forms.ImageField(required=False)

class EnderecoForm(forms.ModelForm):

    class Meta:
        model = Endereco
        fields = ['id', 'cep', 'endereco', 'bairro', 'cidade']


class NaturalidadeForm(forms.ModelForm):

    class Meta:
        model = Naturalidade
        fields = ['id', 'pais', 'cidade', 'uf']


class RegistroGeralForm(forms.ModelForm):

    class Meta:
        model = RegistroGeral
        fields = ['id', 'rg', 'orgao_expedidor', 'data_expedicao', 'uf']

    orgao_expedidor = forms.CharField(label='Órgão Expedidor', required=False)
    data_expedicao = forms.DateField(
        input_formats=['%m/%d/%Y'], label='Data de Expedição', required=False)


class EmailForm(forms.ModelForm):

    class Meta:
        model = Email
        fields = ['id', 'endereco']

    email = forms.EmailField(label='Email', required=False)