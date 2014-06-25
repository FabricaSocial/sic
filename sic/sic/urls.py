from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'sic.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', 'auth.views.inicio'),
                       url(r'^home/$', 'app.views.index'),
                       url(r'^painel/$', 'app.views.painel_controle'),
                       url(r'^painel/ponto/$', 'app.views.alterar_ponto'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('ponto.urls')),
                       url(r'^login/', include('auth.urls')),
                       )
