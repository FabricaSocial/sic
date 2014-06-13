from django.conf.urls import patterns, include, url

urlpatterns = patterns('ponto.views',
                       url(r'ponto/$', 'ponto'),
                       url(r'ponto/registro/$', 'registro'),
                       )
