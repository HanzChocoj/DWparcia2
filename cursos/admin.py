from django.contrib import admin
from .models import Video, Usuario


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'creado_en')
    search_fields = ('titulo',)


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'fecha_registro')
    search_fields = ('nombre', 'correo')
