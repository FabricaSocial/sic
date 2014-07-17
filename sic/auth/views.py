# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from auth.forms import FuncionarioForm, PessoaForm
from modelos.funcionario import Funcionario

# Erros de Login
USUARIO_INATIVO = 1
LOGIN_INVALIDO = 2


def inicio(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    else:
        return render_to_response(
            'login.html',
            context_instance=RequestContext(request)
        )


def entrar(request):
    usuario = request.POST['usuario']
    senha = request.POST['senha']

    login_usuario = authenticate(username=usuario, password=senha)
    erro_login = None

    if login_usuario.last_login != login_usuario.date_joined:
        if login_usuario is not None:
            if login_usuario.is_active:
                login(request, login_usuario)
                return HttpResponseRedirect('/home/')
            else:
                erro_login = USUARIO_INATIVO
        else:
            erro_login = LOGIN_INVALIDO
    else:
        login(request, login_usuario)
        return HttpResponseRedirect('/primeiro-login/')

    return render_to_response(
        'login.html',
        {'erro_login': erro_login},
        context_instance=RequestContext(request)
    )


@login_required(login_url='/login/')
def alterar_senha(request):
    senha = request.POST['senha']
    usuario = request.user

    usuario.set_password(senha)
    usuario.save()

    return render_to_response(
        'home.html',
        {'sucesso': True},
        context_instance=RequestContext(request)
    )


@login_required(login_url='/login/')
def sair(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/login')
def alterar_dados(request):
    usuario = request.user
    alterado = False
    if request.method == 'POST':
        form = request.POST

        alterado = preenche_form(form, usuario)

    forms = obter_forms(usuario)

    return render(request, 'alterar_dados.html', {
        'form_funcionario': forms['funcionario'],
        'form_pessoa': forms['pessoa'],
        'sucesso': alterado,
    })


@login_required(login_url='/login/')
def primeiro_login(request):
    usuario = request.user

    forms = obter_forms(usuario)
    return render_to_response(
        'alterar_dados.html', {
            'primeiro_login': True,
            'form_funcionario': forms['funcionario'],
            'form_pessoa': forms['pessoa'], },
        context_instance=RequestContext(request)
    )


def obter_forms(usuario):
    forms = {}
    funcionario = Funcionario.objects.get(usuario_id=usuario.id)
    forms['funcionario'] = FuncionarioForm(instance=funcionario)

    pessoa = funcionario.pessoa
    forms['pessoa'] = PessoaForm(instance=pessoa)

    return forms


def preenche_form(form, usuario):

    funcionario_antigo = Funcionario.objects.get(usuario_id=usuario.id)
    funcionario = FuncionarioForm(form, instance=funcionario_antigo)

    pessoa_antiga = funcionario_antigo.pessoa
    pessoa = PessoaForm(form, instance=pessoa_antiga)

    sucesso = salvar_formulario(funcionario) and salvar_formulario(pessoa)

    return sucesso


def salvar_formulario(formulario):
    if formulario.is_valid():
        formulario.save()
        return True
    return False
