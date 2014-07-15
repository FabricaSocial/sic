# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from lista_telefonica.forms import FuncionarioForm
from modelos.funcionario import Funcionario


def alterar_dados(request):
    if request.method == 'POST':
        novoFuncionario = FuncionarioForm(request.POST)

        if novoFuncionario.is_valid():
            antigoFuncionario = Funcionario.objects.get(
                matricula=novoFuncionario.matricula)

            novoFuncionario = FuncionarioForm(
                request.POST, instance=antigoFuncionario)

            novoFuncionario.save()

            return HttpResponseRedirect('home.html')
    else:
        formFuncionario = FuncionarioForm()

    return render(request, '', {
        'form': formFuncionario,
    })
