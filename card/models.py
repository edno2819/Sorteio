from django.db import models
from django.utils.html import format_html
from django.contrib import admin


class Disciplina(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=40, blank=False, null=False)

    def __str__(self):
        return self.nome


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=40, blank=False, null=False)
    disciplina = models.ForeignKey(
        "Disciplina", on_delete=models.CASCADE, blank=False, null=False
    )    
    link = models.CharField(max_length=300, blank=False, null=False)
    quantidade = models.SmallIntegerField( blank=False, null=False)

    def __str__(self):
        return self.nome

    @admin.display(ordering="Ativar")
    def link_admin(self):
        return format_html(
            """
        <button style="
            border-radius: 13px;
            background-color: #4CAF50; /* Green */
            border: none;
            color: white;
            padding: 7px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            "
        >
        <a style="text-decoration: none; color: white;" href="{}" target="_blank">Click aqui para abrir</a>
        </button>
        """,
            self.link,
        )