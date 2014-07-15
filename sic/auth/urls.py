from django.conf.urls import patterns, url

urlpatterns = patterns('auth.views',
                       url(r'^$', 'inicio'),
                       url(r'^entrar/$', 'entrar'),
                       url(r'^sair/$', 'sair'),
                       url(r'^alterar-senha/$', 'alterar_senha'),
                       url(r'^alterar-dados/$', 'alterar_dados'),
                       )
