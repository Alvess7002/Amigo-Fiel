from django.db import models


class ProdutoPet(models.Model):
    nome = models.CharField(max_length=120)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.IntegerField()
    categoria = models.CharField(max_length=60)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.nome
