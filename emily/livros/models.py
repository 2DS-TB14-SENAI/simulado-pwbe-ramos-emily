from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=30, blank=True, null=True)
    autor =  models.CharField(max_length=30, blank=True, null=True)
    paginas = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.titulo 