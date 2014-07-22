# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


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


@csrf_protect
def entrar(request):
    usuario = request.POST['usuario']
    senha = request.POST['senha']

    login_usuario = authenticate(username=usuario, password=senha)
    erro_login = None

    if login_usuario is not None:
        if login_usuario.last_login != login_usuario.date_joined:
            if login_usuario.is_active:
                login(request, login_usuario)
                return HttpResponseRedirect('/home/')
            else:
                erro_login = USUARIO_INATIVO
        else:
            login(request, login_usuario)
            return HttpResponseRedirect('/primeiro-login/')
    else:
        erro_login = LOGIN_INVALIDO

    return render_to_response(
        'login.html',
        {'erro_login': erro_login},
        context_instance=RequestContext(request)
    )


@csrf_protect
@login_required(login_url='/login/')
@csrf_protect
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


@login_required(login_url='/login/')
def primeiro_login(request):
    return render_to_response(
        'home.html', {
            'primeiro_login': True, },
        context_instance=RequestContext(request)
    )
