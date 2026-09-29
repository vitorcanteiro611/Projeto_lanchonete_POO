class Cliente:

    def __init__(self, nome, cpf, tel, email, endereco):
        self.nome = nome            
        self.cpf=cpf
        self.__telefone=tel #privado
        self.email=email
        self.endereco=endereco  


    def imprimirCliente(self):            
        print(f"\n--------Cliente {self.nome} ----------- "
                f"\nCpf: {self.cpf}" 
                f"\nTelefone: {self.__telefone}" 
                f"\nE-mail: {self.email}"
                f"\nEndereço:{self.endereco}"
                    )

































##Ver qual precisa ser encapsulado
    #def getTelefone(self):
        #return self.__telefone

    #def setTelefone(self, tel):
        #self.__telefone=tel

        #novoCliente = Cliente(endereco="Rua Vital Brasil", email='joao@gmial.com',
                            #cpf='00000000000', nome='Joao Desenvolvedor', tel='6799999999')
        #novoCliente.imprimeFicha()