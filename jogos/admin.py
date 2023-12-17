from django.contrib import admin
from jogos.models import Jogos, Certificados, quemSou, softSkills, hardSkills


class ListandoJogos(admin.ModelAdmin):
     list_display = ("id", "nome", "legenda", "publicada")
     list_display_links = ("id", "nome")
     search_fields = ("nome",)
     list_filter = ("engine",)
     list_editable = ("publicada",)
     list_per_page = 10

admin.site.register(Jogos, ListandoJogos)


class ListandoCertificados(admin.ModelAdmin):
     list_display = ("id", "nome", "legenda", "publicada")
     list_display_links = ("id", "nome")
     search_fields = ("nome",)
     list_filter = ("engine",)
     list_editable = ("publicada",)
     list_per_page = 10

admin.site.register(Certificados, ListandoCertificados)


class ListandoQuemSou(admin.ModelAdmin):
     list_display = ("id",)
     list_display_links = ("id",)
     list_per_page = 10

admin.site.register(quemSou, ListandoQuemSou)


class ListandoSoftSkills(admin.ModelAdmin):
     list_display = ("id", "skill","publicada",)
     list_display_links = ("id", "skill")
     search_fields = ("skill",)
     list_editable = ("publicada",)
     list_per_page = 10

admin.site.register(softSkills, ListandoSoftSkills)


class ListandoHardSkills(admin.ModelAdmin):
     list_display = ("id", "skill","publicada",)
     list_display_links = ("id", "skill")
     search_fields = ("skill",)
     list_editable = ("publicada",)
     list_per_page = 10

admin.site.register(hardSkills, ListandoHardSkills)
