from django.shortcuts import render, get_object_or_404
from jogos.models import Jogos, Certificados, quemSou, softSkills, hardSkills


def index(request):
    jogos = Jogos.objects.order_by("data_jogo").filter(publicada = True)
    return render(request, 'jogos/index.html', {"cards": jogos})


def jogo(request, jogo_id):
    jogo = get_object_or_404(Jogos, pk=jogo_id)
    return render(request, 'jogos/jogo.html', {"jogo": jogo})

def certificados(request):
    certificados = Certificados.objects.order_by("data_certificado").filter(publicada = True)
    return render(request, 'jogos/certificados.html', {"cards": certificados})


def certificado(request, certificado_id):
    certificado = get_object_or_404(Certificados, pk=certificado_id)
    return render(request, 'jogos/certificado.html', {"certificado": certificado})


def buscar(request):
    jogos = Jogos.objects.order_by("data_jogo").filter(publicada = True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            jogos = jogos.filter(nome__icontains=nome_a_buscar)

    return render (request, "jogos/buscar.html", {"cards": jogos})


def buscarCertificado(request):
    certificados = Certificados.objects.order_by("data_certificado").filter(publicada = True)

    if "buscarCertificado" in request.GET:
        nome_a_buscar = request.GET['buscarCertificado']
        if nome_a_buscar:
            certificados = certificados.filter(nome__icontains=nome_a_buscar)

    return render (request, "jogos/buscarCertificado.html", {"cards": certificados})


def sobreMim(request):
    quem_sou = quemSou.objects.all()
    soft_skills = softSkills.objects.filter(publicada = True)
    hard_skills = hardSkills.objects.filter(publicada = True)
    return render(request, 'jogos/sobreMim.html', {"quemSou": quem_sou,
                                                   "softSkills": soft_skills,
                                                   "hardSkills": hard_skills})