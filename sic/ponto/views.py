# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

# Create your views here.


def ponto(request):
    return render_to_response('ponto_home.html')
