import graphene

from clients_design.schema import ClienteType, ProfissionalType, SecaoMarcadaType
from clients_design.models import Cliente, Profissional, SecaoMarcada


class CriarCliente(graphene.Mutation):
    id = graphene.Int()
    nome = graphene.String()
    sobrenome = graphene.String()

    #2
    class Arguments:
        nome = graphene.String()
        sobrenome = graphene.String()

    cliente = graphene.Field(ClienteType)

    #3
    def mutate(self, info, nome, sobrenome):
        cliente = Cliente(nome=nome,
                          sobrenome=sobrenome)
        cliente.save()

        return CriarCliente(id=cliente.id,
                            nome=cliente.nome,
                            sobrenome=cliente.sobrenome)

class CriarProfissional(graphene.Mutation):
    id = graphene.Int()
    nome = graphene.String()
    sobrenome = graphene.String()

    #2
    class Arguments:
        nome = graphene.String()
        sobrenome = graphene.String()

    profissional = graphene.Field(ProfissionalType)

    #3
    def mutate(self, info, nome, sobrenome):
        profissional = Profissional(nome=nome,
                          sobrenome=sobrenome)
        profissional.save()

        return CriarProfissional(id=profissional.id,
                            nome=profissional.nome,
                            sobrenome=profissional.sobrenome)

class CriarSecao(graphene.Mutation):
    id = graphene.Int()
    data_secao = graphene.DateTime()
    cliente_id = graphene.Int()
    profissional_id = graphene.Int()

    #2
    class Arguments:
        data_secao = graphene.DateTime()
        cliente_id = graphene.Int()
        profissional_id = graphene.Int()

    secao = graphene.Field(SecaoMarcadaType)

    #3
    def mutate(self, info, data_secao, cliente_id,profissional_id):
        cliente = Cliente.objects.get(pk=cliente_id)
        profissional = Profissional.objects.get(pk=profissional_id)

        secao = SecaoMarcada(data_secao=data_secao,
                             cliente_id=cliente,
                             profissional_id=profissional)
        secao.save()

        return CriarSecao(secao=secao)