from django import forms
from .models import Video, Usuario


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['titulo', 'descripcion', 'url', 'duracion']
        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
            'url': 'Enlace de video',
            'duracion': 'Duración',
        }


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'bio', 'videos_inscritos']
        labels = {
            'nombre': 'Nombre',
            'correo': 'Correo electrónico',
            'bio': 'Biografía',
            'videos_inscritos': 'Videos Inscritos (mantén pulsado Ctrl para múltiples)'
        }
        widgets = {
            'videos_inscritos': forms.CheckboxSelectMultiple(),
        }
