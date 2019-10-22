import graphene
from graphene_django.types import DjangoObjectType
from .models import Cliente, Profissional, SecaoMarcada, Produtos, ItensConsumidos

class ClienteType(DjangoObjectType):
    class Meta:
        model = Cliente

class ClienteQuery(graphene.ObjectType):
    all_clientes = graphene.List(ClienteType)

    def resolve_all_clientes(self, info, **kwargs):
        return Cliente.objects.all()

class ProfissionalType(DjangoObjectType):
    class Meta:
        model = Profissional

class ProfissionalQuery(graphene.ObjectType):
    all_profissional = graphene.List(ProfissionalType)

    def resolve_all_profissional(self, info, **kwargs):
        return Profissional.objects.all()


class SecaoMarcadaType(DjangoObjectType):
    class Meta:
        model = SecaoMarcada



class SecaoMarcadaQuery(graphene.ObjectType):
    all_secaomarcada = graphene.List(SecaoMarcadaType)

    def resolve_all_secaomarcada(self, info, **kwargs):
        return SecaoMarcada.objects.all()


class ProdutosType(DjangoObjectType):
    class Meta:
        model = Produtos

class ProdutosQuery(graphene.ObjectType):
    all_produtos = graphene.List(ProdutosType)

    def resolve_all_produtos(self, info, **kwargs):
        return Produtos.objects.all()

class ItensConsumidosType(DjangoObjectType):
    class Meta:
        model = ItensConsumidos



class ItensConsumidosQuery(graphene.ObjectType):
    all_itensconsumidos = graphene.List(ItensConsumidosType)

    def resolve_all_intensconsumidos(self, info, **kwargs):
        return ItensConsumidos.objects.all()