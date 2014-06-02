# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def ponto(request):
    return render_to_response('ponto_home.html')
