from django.urls import path
from . import views


app_name = 'cursos'


urlpatterns = [
path('', views.video_list, name='videos_list'),
path('videos/', views.video_list, name='videos_list'),
path('videos/nuevo/', views.video_create, name='video_create'),
path('videos/<int:pk>/editar/', views.video_edit, name='video_edit'),
path('videos/<int:pk>/eliminar/', views.video_delete, name='video_delete'),


path('usuarios/', views.usuario_list, name='usuario_list'),
path('usuarios/nuevo/', views.usuario_create, name='usuario_create'),
path('usuarios/<int:pk>/editar/', views.usuario_edit, name='usuario_edit'),


path('creditos/', views.creditos, name='creditos'),
]