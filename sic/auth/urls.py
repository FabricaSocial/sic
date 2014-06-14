from django.conf.urls import patterns, include, url

urlpatterns = patterns('auth.views',
                       url(r'^$', 'inicio'),
                       url(r'^entrar/$', 'entrar'),
                       url(r'^sair/$', 'sair'),
                       )
