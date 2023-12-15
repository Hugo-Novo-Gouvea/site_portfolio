from django.shortcuts import render, get_object_or_404
from jogos.models import Jogos

def index(request):
    jogos = Jogos.objects.order_by("data_jogo").filter(publicada = True)
    return render(request, 'jogos/index.html', {"cards": jogos})

def jogo(request, jogo_id):
    jogo = get_object_or_404(Jogos, pk=jogo_id)
    return render(request, 'jogos/jogo.html', {"jogo": jogo})

def buscar(request):
    jogos = Jogos.objects.order_by("data_jogo").filter(publicada = True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            jogos = jogos.filter(nome__icontains=nome_a_buscar)

    return render (request, "jogos/buscar.html", {"cards": jogos})