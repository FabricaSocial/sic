# -*- coding: utf-8 -*-

from django import forms
from modelos.funcionario import Funcionario
from modelos.pessoa import Pessoa


class FuncionarioForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = ['id', 'departamento', 'ramal']


class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = ['id', 'nome']
