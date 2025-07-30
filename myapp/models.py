from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "Autores"

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Libro(models.Model):
    titulo = models.CharField(max_length=256)
    editorial = models.CharField(max_length=128)
    autor = models.ForeignKey(Autor, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.titulo} ({self.autor.apellido})"

