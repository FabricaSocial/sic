# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from auth.forms import FuncionarioForm, PessoaForm, \
    NaturalidadeForm, EnderecoForm, RegistroGeralForm, EmailForm

from modelos.funcionario import Funcionario
from modelos.pessoa import Endereco, RegistroGeral, Email, Naturalidade

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

    if login_usuario is not None:
        if login_usuario.is_active:
            login(request, login_usuario)
            return HttpResponseRedirect('/home/')
        else:
            erro_login = USUARIO_INATIVO
    else:
        erro_login = LOGIN_INVALIDO

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
    if request.method == 'POST':

        form = request.POST
        foto = request.FILES

        preenche_form(form, foto, usuario)
        return HttpResponseRedirect('/home')

    forms = obter_forms(usuario)

    return render(request, 'alterar_dados.html', {
        'form_funcionario': forms['funcionario'],
        'form_pessoa': forms['pessoa'],
        'form_endereco': forms['endereco'],
        'form_email': forms['email'],
        'form_naturalidade': forms['naturalidade'],
        'form_registro_geral': forms['registro_geral'],
    })


def obter_forms(usuario):
    forms = {}
    funcionario = Funcionario.objects.get(usuario_id=usuario.id)
    forms['funcionario'] = FuncionarioForm(instance=funcionario)

    pessoa = funcionario.pessoa
    forms['pessoa'] = PessoaForm(instance=pessoa)

    endereco = Endereco.objects.get(pessoa=pessoa.id)
    forms['endereco'] = EnderecoForm(instance=endereco)

    naturalidade = Naturalidade.objects.get(id=pessoa.naturalidade.id)
    forms['naturalidade'] = NaturalidadeForm(instance=naturalidade)

    try:
        email = Email.objects.get(pessoa=pessoa)
        forms['email'] = EmailForm(instance=email)
    except ObjectDoesNotExist:
        forms['email'] = EmailForm()

    try:
        registro_geral = RegistroGeral.objects.get(pessoa=pessoa)
        forms['registro_geral'] = RegistroGeralForm(instance=registro_geral)
    except ObjectDoesNotExist:
        forms['registro_geral'] = RegistroGeralForm()

    return forms


def preenche_form(form, foto, usuario):

    funcionario_antigo = Funcionario.objects.get(usuario_id=usuario.id)
    funcionario = FuncionarioForm(form, instance=funcionario_antigo)
    salvar_formulario(funcionario)

    pessoa_antiga = funcionario_antigo.pessoa
    pessoa = PessoaForm(form, foto, instance=pessoa_antiga)
    salvar_formulario(pessoa)

    endereco_antigo = pessoa_antiga.endereco
    endereco = EnderecoForm(form, instance=endereco_antigo)
    salvar_formulario(endereco)

    naturalidade_antiga = pessoa_antiga.naturalidade
    naturalidade = NaturalidadeForm(form, instance=naturalidade_antiga)
    salvar_formulario(naturalidade)

    email_antigo = Email.objects.get_or_create(pessoa_id=pessoa_antiga.id)
    email_antigo[0].save()
    email = EmailForm(form, instance=email_antigo[0])
    salvar_formulario(email)

    registro_geral_antigo = RegistroGeral.objects.get_or_create(pessoa_id=pessoa_antiga.id)
    registro_geral_antigo[0].save()
    registro_geral = RegistroGeralForm(form, instance=registro_geral_antigo[0])
    salvar_formulario(registro_geral)


def salvar_formulario(formulario):
    if formulario.is_valid():
        formulario.save()