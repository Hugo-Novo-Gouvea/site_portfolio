from django.urls import path
from jogos.views import index, jogo, certificados, certificado, buscar, buscarCertificado

urlpatterns = [ 
    path('', jogo, name='jogo'),
    #path('jogo/<int:jogo_id>', jogo, name='jogo'),
    path('certificados', certificados, name='certificados'),
    path('ceritifcado/<int:certificado_id>', certificado, name='certificado'),
    path("buscar", buscar, name="buscar"),
    path("buscarCertificado", buscarCertificado, name="buscar"),
]