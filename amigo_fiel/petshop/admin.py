from django.contrib import admin

from .models import ProdutoPet


@admin.register(ProdutoPet)
class ProdutoPetAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "estoque", "categoria")
    search_fields = ("nome", "categoria")
    list_filter = ("categoria",)
