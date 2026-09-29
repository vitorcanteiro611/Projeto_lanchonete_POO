# Projeto lanchonete🥪
Esse projeto marca o início das aulas de programação orientada a objetos com python
da turma de **Técnico de Desenvolvimento de sistemas 2026👨‍💻** 
Projeto pensado na gestão de uma lanchonete fícticia, pensando na parte:
1. Clientes
2. Lanchonete
3. Pedido
4. Itens pedidos
5. Produtos

## Porque a linguagem python foi escolhida para começar esse projeto ao invés de java?🤔 ##

Nesta disciplina, o professor optou por utilizar a linguagem de programação Python 
em vez de Java, pois já estamos familiarizados com Python e estamos desenvolvendo 
nossos conhecimentos nessa linguagem em outras disciplinas.

Como ainda não temos muito conhecimento sobre Java, começar a utilizar 
uma nova linguagem neste momento poderia dificultar nosso aprendizado e gerar confusão. 
Por isso, a escolha do Python permite que a turma aproveite os conhecimentos 
que já possui, facilitando a compreensão dos conteúdos e o 
desenvolvimento das atividades propostas.

## Entendendo as classes😵‍💫##

Esse projeto utiliza **Programação Orientada a Objetos (POO)** para representar os principais elementos 
de uma lanchonete através de classes.

### `Produto`

A classe `Produto` representa os produtos disponíveis no cardápio.

```python
class Produto:
    def __init__(self, nome, cod, preco, descricao, categoria):
        self.nome = nome
        self.cod = cod
        self.preco = preco
        self.descricao = descricao
        self.categoria = categoria
```

Ela armazena informações como nome, código, preço, descrição e categoria do produto.

### `ItemPedido`

A classe `ItemPedido` representa um produto que foi adicionado a um pedido.

```python
class ItemPedido:
    def __init__(self, produto, observacoes, quantidade=1, desconto=0):
        self.produto = produto
        self.observacoes = observacoes
        self.quantidade = quantidade
        self.desconto = desconto
```

Ela permite controlar a quantidade, observações e desconto de cada item.

### `Pedido`

A classe `Pedido` representa o pedido realizado pelo cliente.

```python
class Pedido:
    def __init__(self, numero, data, hora, cliente):
        self.numero = numero
        self.data = data
        self.hora = hora
        self.cliente = cliente
        self.itens = []
```

O pedido possui informações do cliente e uma lista de itens adicionados ao pedido.

### `Cliente`

A classe `Cliente` representa os clientes da lanchonete.

```python
class Cliente:
    def __init__(self, nome, cpf, telefone, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.__telefone = telefone
        self.email = email
        self.endereco = endereco
```

Ela armazena os dados do cliente e utiliza `__telefone` como atributo privado, 
aplicando o conceito de **encapsulamento**.

### Relação entre as classes

As classes se relacionam da seguinte forma:

**Cliente → Pedido → ItemPedido → Produto**

Um cliente realiza um pedido, o pedido possui um ou 
mais itens, e cada item está relacionado a um produto.