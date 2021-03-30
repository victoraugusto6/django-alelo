from django.conf.urls import url
from django.urls import path

from alelo.base.views import home, janeiro, apagar_valor_janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, \
    setembro, outubro, novembro, dezembro, apagar_valor_fevereiro, apagar_valor_marco, apagar_valor_abril, \
    apagar_valor_maio, apagar_valor_junho, apagar_valor_julho, apagar_valor_agosto, apagar_valor_setembro, \
    apagar_valor_outubro, apagar_valor_novembro, apagar_valor_dezembro

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
    path('janeiro/', janeiro, name='janeiro'),
    path('fevereiro/', fevereiro, name='fevereiro'),
    path('marco/', marco, name='marco'),
    path('abril/', abril, name='abril'),
    path('maio/', maio, name='maio'),
    path('junho/', junho, name='junho'),
    path('julho/', julho, name='julho'),
    path('agosto/', agosto, name='agosto'),
    path('setembro/', setembro, name='setembro'),
    path('outubro/', outubro, name='outubro'),
    path('novembro/', novembro, name='novembro'),
    path('dezembro/', dezembro, name='dezembro'),
    url(r'janeiro/delete/(?P<pk>[0-9]+)/$', apagar_valor_janeiro, name='apagar_valor_janeiro'),
    url(r'fevereiro/delete/(?P<pk>[0-9]+)/$', apagar_valor_fevereiro, name='apagar_valor_fevereiro'),
    url(r'marco/delete/(?P<pk>[0-9]+)/$', apagar_valor_marco, name='apagar_valor_marco'),
    url(r'abril/delete/(?P<pk>[0-9]+)/$', apagar_valor_abril, name='apagar_valor_abril'),
    url(r'maio/delete/(?P<pk>[0-9]+)/$', apagar_valor_maio, name='apagar_valor_maio'),
    url(r'junho/delete/(?P<pk>[0-9]+)/$', apagar_valor_junho, name='apagar_valor_junho'),
    url(r'julho/delete/(?P<pk>[0-9]+)/$', apagar_valor_julho, name='apagar_valor_julho'),
    url(r'agosto/delete/(?P<pk>[0-9]+)/$', apagar_valor_agosto, name='apagar_valor_agosto'),
    url(r'setembro/delete/(?P<pk>[0-9]+)/$', apagar_valor_setembro, name='apagar_valor_setembro'),
    url(r'outubro/delete/(?P<pk>[0-9]+)/$', apagar_valor_outubro, name='apagar_valor_outubro'),
    url(r'novembro/delete/(?P<pk>[0-9]+)/$', apagar_valor_novembro, name='apagar_valor_novembro'),
    url(r'dezembro/delete/(?P<pk>[0-9]+)/$', apagar_valor_dezembro, name='apagar_valor_dezembro'),
]
