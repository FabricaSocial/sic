# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf


@login_required(login_url='/login/')
def index(request):
    user = request.user

    if user.groups.filter(name='gerencia').count():
        gerencia = True
    else:
        gerencia = False

    return render_to_response(
        'home.html',
        {'gerencia': gerencia},
        context_instance=RequestContext(request))


def pagina_nao_encontrada(request):
    mensagem_erro = 'A página solicitada não foi encontrada :('

    response = return_erro(request, mensagem_erro)
    return response


def acesso_negado(request):
    mensagem_erro = 'Você não tem permissão para acessar essa página :('

    response = return_erro(request, mensagem_erro)
    return response


def erro_no_sistema(request):
    mensagem_erro = 'Ocorreu um erro no sistema :('

    response = return_erro(request, mensagem_erro)
    return response


def return_erro(request, mensagem_erro):
    csrf_token = {}
    csrf_token.update(csrf(request))
    modal_erro = True

    if request.user.is_authenticated():
        response = redirect('/home/', csrf_token, modal_erro, mensagem_erro)
    else:
        response = redirect('/login/', csrf_token, kwargs={
                            'modal_erro': modal_erro,
                            'mensagem_erro': mensagem_erro})

    return response
