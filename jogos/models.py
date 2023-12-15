from django.db import models
from datetime import datetime

class Jogos(models.Model):
    
    OPCOES_ENGINE = [
        ("UNITY", "Unity"),
        ("UNREAL 5", "Unreal 5"),
    ]

    nome = models.CharField(max_length = 100, null = False, blank = False)
    legenda = models.CharField(max_length = 150, null = False, blank = False)
    engine = models.CharField(max_length = 100,choices = OPCOES_ENGINE, default='')
    descricao = models.TextField(null = False, blank = False)
    imagem = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default = False)
    data_jogo = models.DateTimeField(default = datetime.now, blank = False)

    def __str__(self):
        return self.nome
