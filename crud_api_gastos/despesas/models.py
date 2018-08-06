from django.db import models


class Despesas(models.Model):
    descricao = models.TextField(max_length=150)
    data = models.DateField(auto_now_add=True)
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    comentario = models.TextField()



