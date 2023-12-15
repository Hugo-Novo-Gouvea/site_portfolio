from django.urls import path
from jogos.views import index, jogo, buscar

urlpatterns = [ 
    path('', index, name='index'),
    path('jogo/<int:jogo_id>', jogo, name='jogo'),
    path("buscar", buscar, name="buscar"),
]