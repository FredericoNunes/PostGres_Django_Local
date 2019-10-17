import graphene
from graphene_django.types import DjangoObjectType
from .models import cliente, profissional, secaomarcada

class ClienteType(DjangoObjectType):
    class Meta:
        model = cliente

class Cliente_Query(graphene.ObjectType):
    all_clientes = graphene.List(ClienteType)

    def resolve_all_clientes(self, info, **kwargs):
        return cliente.objects.all()

class ProfissionalType(DjangoObjectType):
    class Meta:
        model = profissional

class Profissional_Query(graphene.ObjectType):
    all_profissional = graphene.List(ProfissionalType)

    def resolve_all_profissional(self, info, **kwargs):
        return profissional.objects.all()


class SecaoMarcadaType(DjangoObjectType):
    class Meta:
        model = secaomarcada

class SecaoMarcada_Query(graphene.ObjectType):
    all_secaomarcada = graphene.List(SecaoMarcadaType)

    def resolve_all_secaomarcada(self, info, **kwargs):
        return secaomarcada.objects.all()

