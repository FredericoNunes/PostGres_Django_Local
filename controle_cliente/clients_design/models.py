from django.db import models

# Create your models here.

class Cliente(models.Model):

    class Meta:
        db_table = '"design"."cliente"'

    #id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Profissional(models.Model):

    class Meta:
        db_table = '"design"."profissional"'

    #id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class SecaoMarcada(models.Model):

    class Meta:
        db_table = '"design"."secao"'

    #id = models.AutoField(primary_key=True)
    data_secao = models.DateTimeField()
    cliente_id = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    profissional_id = models.ForeignKey(Profissional, on_delete=models.DO_NOTHING)

