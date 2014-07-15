from django.conf.urls import patterns, url


urlpatterns = patterns('lista_telefonica',
                       url(r'^lista/$', 'views.listar_telefones'),
                       url(r'^departamentos/$',
                           'views.obter_lista_departamentos_json'),
                       url(r'^funcionarios/(?P<nome>\w*)',
                           'views.obter_lista_funcionarios_json'),
                       )
