# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def index(request):
    return render_to_response('home.html')
