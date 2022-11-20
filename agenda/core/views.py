from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Evento


# Create your views here.

@login_required(login_url='login')
def index(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    return render(request, 'core/index.html', {
        'eventos': evento,  
    }) 

@login_required(login_url='login')
def new_event(request, id=0):
    dados = {}
    usuario = request.user
    if request.POST:
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao_evento')
        data = request.POST.get('data_evento')
        evento_id = request.POST.get('evento_id')
        
        if evento_id:
            evento = get_object_or_404(Evento, pk=id)
            if evento.usuario == usuario:
                Evento.objects.filter(id=evento_id).update(titulo=titulo, data_evento=data, descricao=descricao)
                return redirect('index')

        elif descricao is  None:
            descricao = ''

        Evento.objects.create(titulo=titulo, data_evento=data,descricao=descricao, usuario=usuario)
        return redirect('index')
    elif id:
        evento = get_object_or_404(Evento, pk=id)
        if evento.usuario == usuario:
            dados['evento'] = evento
        return render(request, 'core/novo_evento.html', dados)

    return render(request, 'core/novo_evento.html', dados)

@login_required(login_url='login')
def detalhes(request, id):
    return render(request, 'core/')
    

def login_user(request):
    return render(request, 'core/login.html', {})

def register_user(request):
    if request.POST:
        username = request.POST.get('usuario')
        email = request.POST.get('email')
        password = request.POST.get('password')
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        return redirect('login')
    else:
        return render(request, 'core/register.html')

def submit_login(request):
    if request.POST:
        nome = request.POST.get('usuario')
        senha = request.POST.get('password')
        usuario = authenticate(username=nome, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha invalidos')
    return redirect('index')

def logout_user(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = get_object_or_404(Evento, pk=id_evento)
    if evento.usuario == usuario:
        evento.delete()
    return redirect('/')