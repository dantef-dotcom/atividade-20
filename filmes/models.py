from django.db import models


class Diretor(models.Model):
    nome = models.CharField(max_length=120)
    nacionalidade = models.CharField(max_length=80, blank=True)

    class Meta:
        verbose_name = "Diretor"
        verbose_name_plural = "Diretores"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=80, unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    ano_lancamento = models.PositiveIntegerField()
    sinopse = models.TextField(blank=True)
    diretor = models.ForeignKey(
        Diretor,
        on_delete=models.PROTECT,
        related_name="filmes"
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="filmes"
    )

    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"
        ordering = ["titulo"]

    def __str__(self):
        return f"{self.titulo} ({self.ano_lancamento})"