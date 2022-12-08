from django.contrib import admin

from card.models import *


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ["nome"]

    class Meta:
        model = Disciplina

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_editable = ["link","quantidade"]
    search_fields = ["nome"]
    list_filter = ["nome",]
    list_display = ["nome", "disciplina", "quantidade", "link"]

    class Meta:
        model = Card