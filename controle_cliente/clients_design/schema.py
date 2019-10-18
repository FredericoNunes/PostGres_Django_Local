import graphene
from graphene_django.types import DjangoObjectType
from .models import Cliente, Profissional, SecaoMarcada

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

