class Pedido:
    #não difinir os atributos
    status="Recebido"

    #método construtor - instaciar recebe o valor dos objetos
    def __init__(self, numero, data, hora, cliente, itens, pag):
        #self é chamar os atributos;
        self.numero = numero
        self.data = data
        self.hora = hora
        self.cliente = cliente
        self.itens = itens
        self.pagamento = pag

    
    #Metódo - Ação
    #def  atualizar_Pedido(self, novoStatus):
     #   self.status=novoStatus

    def imprimirPedido(self):           
        print(f"\n--------Pedido n° {self.numero} ----------- "
              f"\nData: {self.data}" 
              f"\nHora: {self.hora}"
              f"\nCliente:{self.cliente.nome}" 
              f"\nPagamento: {self.pagamento} - Status{self.status}"
            )

        for item in self.itens:
            print(f'Produto: {item.produto.descricao}'
                f'- Qtd: {item.quantidade} - Valor:{item.produto.preco}'
                f'Total: {item.totalItem()}'        
                )
        