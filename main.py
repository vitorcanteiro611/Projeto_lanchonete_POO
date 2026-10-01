import os
os.system('cls')

from Produto import Produto
from ItemPedido import ItemPedido
from Cliente import Cliente
from Pedido import Pedido

def menuCliente():
     while True:
        os.system('cls')
        print("--------👤Cad Clientes--------\n"
              "1 - 👤 Adicionar\n"+
              "2 - 📦 Listar\n"+
              "3 - 🔍 Buscar\n"+
              "4 - ❌ Excluir\n"+
              "0 - ⬅️ Sair")
        opcao = input("Digite a opção escolhida:")

        if opcao=="0":
            break


def menuProduto():
    while True:
            os.system('cls')
            print("--------📦Produtos--------\n"
                  "1 - 📦Adicionar\n"+
                  "2 - 📄 Listar\n"+
                  "3 - 🔍 Buscar\n"+
                  "4 - ❌ Excluir\n"+
                  "0 - ⬅️ Sair")
            opcao = input("Digite a opção escolhida:")

            if opcao=="0":
                break




#def munuPedido():




while True:
    os.system('cls')
    print("--------Sistema Lanchonete🥪--------\n"
          "1 - 👤 Clientes\n"+
          "2 - 📦 Produtos\n"+
          "3 - 🛒 Novo Pedido\n"+
          "0 - ⬅️ Sair\n")
    

    opcao = input("Digite a opção escolhida:")

    if opcao=="0":
        break
    elif opcao=="1":
        menuCliente()

    elif opcao=="2":
        menuProduto()

print("Até mais usuário👋\n\n")    




















































#Cadastrar cliente
#novoCli = Cliente(nome='Amado Vitor', cpf='010.378.281-57',
 #                 email='amadodograu99@mail.com', endereco="Rua de pedra, n°00", tel="(67)99999-9999")


#Cadastrar produto

#Hambúrguer = Produto(cod=0, nome='Siriguaijo', descricao= 'Pão e carne', categoria= 'Lanche', 
 #                    preco=76.99)

#refri = Produto(cod=1, nome='Refrizin', descricao='Agua com gás e corante', categoria='Bebida Energética',
             #   preco=15.00)

#novoCli.imprimirCliente()
#Hambúrguer.imprimeProduto()
#efri.imprimeProduto()

#Pedido
#item1 = ItemPedido(produto = Hambúrguer, observacoes="Pouco pão", qtd=3, desconto=4)
#item2 = ItemPedido(produto = refri, observacoes="Muito quente", qtd=2, desconto=0)

#itens = [item1, item2]

#pedido = Pedido(numero=5, data='28/09/2026', hora='12:00', cliente=novoCli,
          #      itens=itens, pag='pix')

#pedido.imprimirPedido()


































#____________________________________________________________________________________________________________________________
#produto_Xbacon = Produto(nome="X-Bacon",cod= "P01", preco=15.00, descricao="Pão, bacon e cebola", categoria="Lanches")

#imprimeProduto = produto_Xbacon.imprimeProduto()

#item1 = ItemPedido(produto=produto_Xbacon, observacoes="Sem cebola")
#print(f"Produto: {item1.produto.nome}"
      #f"\nObservações: {item1.obsservacoes}")


#print("\n--- Atualizando o item do pedido ---")

#item1.atualizar_item(novo_produto=produto_Xbacon, novas_observacoes="Com cebola")
#print(f"Produto: {item1.produto.nome}"
#      f"\nObservações: {item1.obsservacoes}")

#imprimirPedido = item1.imprimirPedido()
#atualizar_observacoes = item1.atualizar_observacoes(novas_observacoes="Sem alface")
#atualizar_produto = item1.atualizar_produto(novo_produto=produto_Xbacon)
#atualizar_item = item1.atualizar_item(novo_produto=produto_Xbacon, novas_observacoes="Sem tomate")
#atualizar_item_completo = item1.atualizar_item_completo(novo_produto=produto_Xbacon, novas_observacoes="Com alface")

#_____________________________________________________________________________________________________________________________

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