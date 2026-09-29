class ItemPedido:
    def __init__(self, produto, observacoes, qtd, desconto):
        self.produto = produto
        self.observacoes = observacoes
        self.quantidade = qtd
        self.desconto=desconto


    def imprimirPedido(self):
        print(f"Produto: {self.produto.nome}" 
              f"\nObservações: {self.obsservacoes}")

    def totalItem(self):
        total = (self.produto.preco * self.quantidade) - self.desconto
        return total
    #def atualizar_observacoes(self, novas_observacoes):
       # self.obsservacoes = novas_observacoes

    #def atualizar_produto(self, novo_produto):
      #  self.produto = novo_produto

    #def atualizar_item(self, novo_produto, novas_observacoes):
     #   self.produto = novo_produto
     #   self.obsservacoes = novas_observacoes

    #def atualizar_item_completo(self, novo_produto, novas_observacoes):
    #    self.produto = novo_produto
    #    self.obsservacoes = novas_observacoes
