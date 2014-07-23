# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf

# Erros de Login
USUARIO_INATIVO = 1
LOGIN_INVALIDO = 2


def inicio(request):
    if request.user.is_authenticated():
        return redirect('/home/')
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

    csrf_token = {}
    csrf_token.update(csrf(request))    
    
    if login_usuario is not None:
        if login_usuario.last_login != login_usuario.date_joined:
            if login_usuario.is_active:
                login(request, login_usuario)
                return redirect('/home/', csrf_token)
            else:
                erro_login = USUARIO_INATIVO
        else:
            login(request, login_usuario)
            return redirect('/primeiro-login/', csrf_token)
    else:
        erro_login = LOGIN_INVALIDO

    return render_to_response(
        'login.html',
        {'erro_login': erro_login, 'modal_erro': True},
        context_instance=RequestContext(request)
    )


@login_required(login_url='/login/')
@ensure_csrf_cookie
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
    return redirect('/')


@login_required(login_url='/login/')
def primeiro_login(request):
    return render_to_response(
        'home.html', {
            'primeiro_login': True, },
        context_instance=RequestContext(request)
    )
