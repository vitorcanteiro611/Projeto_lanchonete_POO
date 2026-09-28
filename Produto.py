class Produto:

    def __init__(self, nome, cod, preco, descricao, categoria):  #parametros do construtor
        self.nome = nome   #self é o objeto que está sendo instanciado, ou seja, o objeto que está sendo criado
        self.preco = preco  
        self.descricao = descricao  #atributos da classe Produto
        self.codigo=cod 
        self.categoria=categoria 


    def imprimeProduto(self):
        print(
            f"\n--------Produto cód. {self.codigo}--------"
            f"\nDescrição: {self.descricao}"
            f"\nCategoria: {self.categoria}"
            f"\nValor: R$ {self.preco:.2f}"
            f"\n------------------------------------------"
        )
        