import os
os.system('cls')

from Produto import Produto
from ItemPedido import ItemPedido


produto_Xbacon = Produto(nome="X-Bacon",cod= "P01", preco=15.00, descricao="Pão, bacon e cebola", categoria="Lanches")

imprimeProduto = produto_Xbacon.imprimeProduto()

item1 = ItemPedido(produto=produto_Xbacon, observacoes="Sem cebola")
print(f"Produto: {item1.produto.nome}"
      f"\nObservações: {item1.obsservacoes}")


print("\n--- Atualizando o item do pedido ---")

item1.atualizar_item(novo_produto=produto_Xbacon, novas_observacoes="Com cebola")
print(f"Produto: {item1.produto.nome}"
      f"\nObservações: {item1.obsservacoes}")

imprimirPedido = item1.imprimirPedido()
atualizar_observacoes = item1.atualizar_observacoes(novas_observacoes="Sem alface")
atualizar_produto = item1.atualizar_produto(novo_produto=produto_Xbacon)
atualizar_item = item1.atualizar_item(novo_produto=produto_Xbacon, novas_observacoes="Sem tomate")
atualizar_item_completo = item1.atualizar_item_completo(novo_produto=produto_Xbacon, novas_observacoes="Com alface")











#from Pedido import Pedido
#from Cliente import Cliente  # type: ignore # Classe cliente foi importada da outra aba

# 1. Primeiro, obsjeto cliente foi criado com os dados do cliente
#cliente_gabriel = Cliente(nome="Gabriel Cristaldo", tel="11 98888-7777", cpf='100.284.291-67', email='gabriel@gmail.com', endereco='Avenida Brasil')

# 2. Agora, agora o objeto 'cliente_gabriel' dentro do construtor do Pedido
#novoPedido = Pedido(
    #numero=1,
    #data="16/09/2026", 
    #hora="21:10", 
    #cliente=cliente_gabriel,  # Aqui entra o objeto cliente, no caso o Gabriel
    #itens=["X-Salada", "X-Bacon"], 
    #pag="Pix"
#)
# ------------------------------------------------------------------#

# Acessar um atributo do objeto
#print(f"Número do pedido: {novoPedido.numero}")
      
#print(f"Status inicial: {novoPedido.status}")


# Chamando os métodos (as ações que o def guardou)
#novoPedido.imprimir()

#print("\n--- Atualizando o status ---")
# Forma correta (passando pelo botão 'def' que você criou):
#novoPedido.atualizar_Pedido("Em preparo")

# Mostrando o status atualizado
#print(f"Status atual: {novoPedido.status}")
#print('-'*5) para colocar o numero de linhas

