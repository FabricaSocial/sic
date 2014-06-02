from django.conf.urls import patterns, include, url
from django.contrib import admin
import ponto
admin.autodiscover()

urlpatterns = patterns('ponto.views',
                       url(r'^$', 'ponto'),
                       )
