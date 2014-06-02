from django.conf.urls import patterns, include, url

urlpatterns = patterns('ponto.views',
                       url(r'^$', 'ponto'),
                       )
