from django.conf.urls import patterns, url


urlpatterns = patterns('lista_telefonica',
                       url(r'^lista/$', 'views.listar_telefones'),
                       url(r'^teste/$', 'request.alterar_dados'),
                       )
