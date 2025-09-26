from django.db import models


class Video(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    url = models.URLField(verbose_name='URL (YouTube u otro)', blank=True)
    duracion = models.CharField(max_length=50, blank=True, help_text='Ej: 12:34')
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Usuario(models.Model):
    nombre = models.CharField(max_length=150)
    correo = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    videos_inscritos = models.ManyToManyField(Video, blank=True, related_name='estudiantes')

    def __str__(self):
        return self.nombre
