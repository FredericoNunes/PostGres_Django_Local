import graphene
from clients_design.schema import Cliente_Query, Profissional_Query, SecaoMarcada_Query

class Query(Cliente_Query,
            Profissional_Query,
            SecaoMarcada_Query,
            graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)