from django.contrib import admin

from galeria.models import Fotografia

# Register your models here.

class ListandoFotografia(admin.ModelAdmin):
  list_display = ("id", "nome", "legenda", "data_fotografia", "publicada")
  list_display_links = ("id", "nome")
  search_fields = ("nome",)
  list_filter = ("categoria",)
  list_per_page = 10
  list_editable =("publicada",)

admin.site.register(Fotografia, ListandoFotografia)
