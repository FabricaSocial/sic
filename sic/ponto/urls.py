from django.conf.urls import patterns, url

urlpatterns = patterns('ponto.views',
                       url(r'ponto/$', 'ponto'),
                       url(r'ponto/registro/$', 'registro'),
                       url(r'ponto/registro/(?P<matricula>\w*)',
                           'registrar_ponto_ajax')
                       )
