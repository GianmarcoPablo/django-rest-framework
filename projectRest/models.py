from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    technology = models.CharField(max_length=200, verbose_name="Tecnologia")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")