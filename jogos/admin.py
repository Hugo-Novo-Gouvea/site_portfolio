from django.contrib import admin
from jogos.models import Jogos

class ListandoJogos(admin.ModelAdmin):
     list_display = ("id", "nome", "legenda", "publicada")
     list_display_links = ("id", "nome")
     search_fields = ("nome",)
     list_filter = ("engine",)
     list_editable = ("publicada",)
     list_per_page = 10

admin.site.register(Jogos, ListandoJogos)
