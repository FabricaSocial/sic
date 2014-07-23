# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


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
