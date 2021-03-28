from django.urls import path

from alelo.base.views import home, meses, apagar

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
    path('meses/', meses, name='meses'),
    path('apagar/<int:valor_id>', apagar, name='apagar'),
]
