from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^home/$', 'app.views.index'),
                       url(r'^painel/$', 'app.views.painel_controle'),

                       url(r'^$', 'auth.views.inicio'),
                       url(r'^login/', include('auth.urls')),

                       url(r'^painel/ponto/$', 'app.views.alterar_ponto'),
                       url(r'^', include('ponto.urls')),

                       url(r'^telefones/', include('lista_telefonica.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       )
