from django.contrib import admin

from alelo.base.models import Janeiro, Fevereiro, Marco, Abril, Maio, Junho, Julho, Agosto, Setembro, Outubro, Novembro, \
    Dezembro


@admin.register(Janeiro)
class JaneiroAdmin(admin.ModelAdmin):
    list_display = ['valor', 'criado_em']
    ordering = ['criado_em']


@admin.register(Fevereiro)
class FevereiroAdmin(admin.ModelAdmin):
    list_display = ['valor', 'criado_em']
    ordering = ['criado_em']


@admin.register(Marco)
class MarcoAdmin(admin.ModelAdmin):
    list_display = ['valor', 'criado_em']
    ordering = ['criado_em']


@admin.register(Abril)
class AbrilAdmin(admin.ModelAdmin):
    list_display = ['valor', 'criado_em']
    ordering = ['criado_em']


@admin.register(Maio)
class MaioAdmin(admin.ModelAdmin):
    list_display = ['valor', 'criado_em']
    ordering = ['criado_em']


@admin.register(Junho)
class JunhoAdmin(admin.ModelAdmin):
    list_display = ['valor', 'criado_em']
    ordering = ['criado_em']


@admin.register(Julho)
class JulhoAdmin(admin.ModelAdmin):
    list_display = ['valor', 'criado_em']
    ordering = ['criado_em']


@admin.register(Agosto)
class AgostoAdmin(admin.ModelAdmin):
    list_display = ['valor', 'criado_em']
    ordering = ['criado_em']


@admin.register(Setembro)
class SetembroAdmin(admin.ModelAdmin):
    list_display = ['valor', 'criado_em']
    ordering = ['criado_em']


@admin.register(Outubro)
class OutubroAdmin(admin.ModelAdmin):
    list_display = ['valor', 'criado_em']
    ordering = ['criado_em']


@admin.register(Novembro)
class NovembroAdmin(admin.ModelAdmin):
    list_display = ['valor', 'criado_em']
    ordering = ['criado_em']


@admin.register(Dezembro)
class DezembroAdmin(admin.ModelAdmin):
    list_display = ['valor', 'criado_em']
    ordering = ['criado_em']
