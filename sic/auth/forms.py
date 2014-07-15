# -*- coding: utf-8 -*-

from django.forms import ModelForm
from modelos.funcionario import Funcionario


class FuncionarioForm(ModelForm):

    class Meta:
        model = Funcionario
        fields = ['matricula', 'status', 'pessoa', 'cargo', 'departamento',
                  'usuario']
