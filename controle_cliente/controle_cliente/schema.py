import graphene
from clients_design.schema import ClienteQuery, ProfissionalQuery, SecaoMarcadaQuery
from clients_design.mutation import CriarCliente, CriarProfissional, CriarSecao

class Query(ClienteQuery,
            ProfissionalQuery,
            SecaoMarcadaQuery,
            graphene.ObjectType):
    pass



class Mutation(graphene.ObjectType):
    criar_cliente = CriarCliente.Field()
    criar_profissional = CriarProfissional.Field()
    criar_secao = CriarSecao.Field()




schema = graphene.Schema(query=Query,mutation=Mutation)