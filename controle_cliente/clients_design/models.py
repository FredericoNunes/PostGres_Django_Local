from django.db import models

# Create your models here.

class cliente(models.Model):

    class Meta:
        db_table = '"design"."cliente"'

    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)

class profissional(models.Model):

    class Meta:
        db_table = '"design"."profissional"'

    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)

class secao_marcada(models.Model):

    class Meta:
        db_table = '"design"."secao"'

    id = models.IntegerField(primary_key=True)
    data_secao = models.DateTimeField()
    cliente_nome = models.ForeignKey(cliente, on_delete=models.DO_NOTHING)
    profissional_nome = models.ForeignKey(profissional, on_delete=models.DO_NOTHING)
