import graphene
from clients_design.schema import ClienteQuery, ProfissionalQuery, SecaoMarcadaQuery, ProdutosQuery, ItensConsumidosQuery
from clients_design.mutation import CriarCliente, CriarProfissional, CriarSecao, CriarProduto, CriarItensConsumidos

class Query(ClienteQuery,
            ProfissionalQuery,
            SecaoMarcadaQuery,
            ProdutosQuery,
            ItensConsumidosQuery,
            graphene.ObjectType):
    pass



class Mutation(graphene.ObjectType):
    criar_cliente = CriarCliente.Field()
    criar_profissional = CriarProfissional.Field()
    criar_secao = CriarSecao.Field()
    criar_produto = CriarProduto.Field()
    criar_itens_consumidos = CriarItensConsumidos.Field()




schema = graphene.Schema(query=Query,mutation=Mutation)