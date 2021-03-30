from django.db import models


class Janeiro(models.Model):
    valor = models.FloatField(max_length=10)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.valor


class Fevereiro(models.Model):
    valor = models.FloatField(max_length=10)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.valor


class Marco(models.Model):
    valor = models.FloatField(max_length=10)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.valor


class Abril(models.Model):
    valor = models.FloatField(max_length=10)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.valor


class Maio(models.Model):
    valor = models.FloatField(max_length=10)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.valor


class Junho(models.Model):
    valor = models.FloatField(max_length=10)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.valor


class Julho(models.Model):
    valor = models.FloatField(max_length=10)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.valor


class Agosto(models.Model):
    valor = models.FloatField(max_length=10)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.valor


class Setembro(models.Model):
    valor = models.FloatField(max_length=10)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.valor


class Outubro(models.Model):
    valor = models.FloatField(max_length=10)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.valor


class Novembro(models.Model):
    valor = models.FloatField(max_length=10)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.valor


class Dezembro(models.Model):
    valor = models.FloatField(max_length=10)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.valor
