from django.conf.urls import patterns, url


urlpatterns = patterns('lista_telefonica.views',
                       url(r'^lista/$', 'listar_telefones'),
                       )
