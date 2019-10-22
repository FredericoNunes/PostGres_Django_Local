import graphene

from clients_design.schema import ClienteType, ProfissionalType, SecaoMarcadaType, ProdutosType, ItensConsumidosType
from clients_design.models import Cliente, Profissional, SecaoMarcada, Produtos, ItensConsumidos


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

class CriarProduto(graphene.Mutation):
    id = graphene.Int()
    nome_produto = graphene.String()
    preco = graphene.Int()

    class Arguments:
        nome_produto = graphene.String()
        preco = graphene.Int()

    produto = graphene.Field(ProdutosType)

    def mutate(self, info, nome_produto, preco):
        produto = Produtos(
            nome_produto=nome_produto,
            preco=preco
        )
        produto.save()

        return CriarProduto(produto=produto)

class CriarItensConsumidos(graphene.Mutation):
    id = graphene.Int()
    secao_id = graphene.Int()
    produto_id = graphene.Int()
    quantidade = graphene.Int()

    #2
    class Arguments:
        secao_id = graphene.Int()
        produto_id = graphene.Int()
        quantidade = graphene.Int()

    itensConsumidos = graphene.Field(ItensConsumidosType)

    #3
    def mutate(self, info, secao_id, produto_id,quantidade):
        secao = SecaoMarcada.objects.get(pk=secao_id)
        produto = Produtos.objects.get(pk=produto_id)

        itensConsumidos = ItensConsumidos(
            secao_id=secao,
            produto_id=produto,
            quantidade=quantidade)

        itensConsumidos.save()

        return CriarItensConsumidos(itensConsumidos=itensConsumidos)
