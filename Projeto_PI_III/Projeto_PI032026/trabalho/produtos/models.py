from django.db import models
from django.utils.text import slugify
import os


def get_upload_path(instance, filename):
    name, ext = os.path.splitext(filename)
    slug = slugify(instance.nome)
    return f'produtos/{slug}-{instance.pk or "novo"}{ext}'


class Produto(models.Model):
    CATEGORIAS = [
        ('lanche', 'Lanche'),
        ('bebida', 'Bebida'),
        ('sobremesa', 'Sobremesa'),
        ('porcao', 'Porção'),
        ('combo', 'Combo'),
        ('pastel', 'Pastel'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    oculto = models.BooleanField(default=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    imagem = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['categoria', 'nome']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = Produto.objects.get(pk=self.pk)
                if old_instance.imagem and old_instance.imagem != self.imagem:
                    old_instance.imagem.delete(save=False)
            except Produto.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.imagem:
            self.imagem.delete(save=False)
        super().delete(*args, **kwargs)