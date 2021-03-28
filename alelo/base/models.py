from django.db import models


class Janeiro(models.Model):
    valor = models.FloatField(max_length=10)
    criado_em = models.DateField(auto_now_add=True)
