from django.urls import path
from jogos.views import index, jogo, certificados, certificado, buscar

urlpatterns = [ 
    path('', index, name='index'),
    path('jogo/<int:jogo_id>', jogo, name='jogo'),
    path('certificados', certificados, name='certificados'),
    path('ceritifcado/<int:certificado_id>', certificado, name='certificado'),
    path("buscar", buscar, name="buscar"),
]