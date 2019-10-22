from django.db import models

# Create your models here.

class Cliente(models.Model):

    class Meta:
        db_table = '"design"."cliente"'
        verbose_name_plural = 'Clientes'


    #id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Profissional(models.Model):

    class Meta:
        db_table = '"design"."profissional"'
        verbose_name_plural = 'Profissionais'

    #id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class SecaoMarcada(models.Model):

    class Meta:
        db_table = '"design"."secao"'
        ordering = ["data_secao"]
        verbose_name_plural = 'Secões Marcadas'

    #id = models.AutoField(primary_key=True)
    data_secao = models.DateTimeField()
    cliente_id = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    profissional_id = models.ForeignKey(Profissional, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.data_secao) + " " + str(self.cliente_id) + " " + str(self.profissional_id)

class Produtos(models.Model):

    class Meta:
        db_table = '"design"."produtos"'
        ordering = ["nome_produto"]
        verbose_name_plural = 'Produtos'

    nome_produto = models.CharField(max_length=100)
    preco = models.IntegerField()

    def __str__(self):
        return self.nome_produto + " " + " - Preço: " + str(self.preco/100)

class ItensConsumidos(models.Model):

    class Meta:
        db_table = '"design"."itensconsumidos"'
        verbose_name_plural = 'Itens Consumidos'

    secao_id = models.ForeignKey(SecaoMarcada, on_delete=models.DO_NOTHING)
    produto_id = models.ForeignKey(Produtos, on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField()

    def __str__(self):
        return str(self.secao_id) + " - " + str(self.produto_id) + " - Quantidade - " + str(self.quantidade)


