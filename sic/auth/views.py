# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

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


def sair(request):
  logout(request)
