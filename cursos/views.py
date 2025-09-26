from django.shortcuts import render, get_object_or_404, redirect
from .models import Video, Usuario
from .forms import VideoForm, UsuarioForm


# VIDEOS

def video_list(request):
    videos = Video.objects.order_by('-creado_en')
    return render(request, 'cursos/videos_list.html', {'videos': videos})



def video_create(request):
    form = VideoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cursos:videos_list')
    return render(request, 'cursos/video_form.html', {'form': form})


def video_edit(request, pk):
    video = get_object_or_404(Video, pk=pk)
    form = VideoForm(request.POST or None, instance=video)
    if form.is_valid():
        form.save()
        return redirect('cursos:videos_list')
    return render(request, 'cursos/video_form.html', {'form': form, 'video': video})


def video_delete(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        video.delete()
        return redirect('cursos:videos_list')
    return render(request, 'cursos/video_confirm_delete.html', {'video': video})


# USUARIOS

def usuario_list(request):
    usuarios = Usuario.objects.order_by('-fecha_registro')
    return render(request, 'cursos/usuarios_list.html', {'usuarios': usuarios})


def usuario_create(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cursos:usuario_list')
    return render(request, 'cursos/usuario_form.html', {'form': form})


def usuario_edit(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    form = UsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('cursos:usuario_list')
    return render(request, 'cursos/usuario_form.html', {'form': form, 'usuario': usuario})



# CREDITOS

def creditos(request):
    return render(request, 'cursos/creditos.html')
