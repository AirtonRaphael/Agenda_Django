from django.shortcuts import render, get_object_or_404
from .models import Evento

# Create your views here.
def index(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    return render(request, 'core/index.html', {
        'eventos': evento,
    }) 