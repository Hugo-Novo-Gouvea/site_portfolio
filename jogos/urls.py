from django.urls import path
from jogos.views import index

urlpatterns = [ 
    path('', index, name='index'),
]