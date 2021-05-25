'''
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, 
com valor default zero e os demais atributos são obrigatórios. 
'''
class ContaCorrente(object):
    def __init__(self, numero, correntista, saldo=0):
        self.numero = numero
        self.correntista = correntista
        self.saldo = saldo
        
    def altera_nome(self, nome):
        self.nome = nome
    
    def deposito(self, qnd):
        self.saldo += qnd
        
    def saque(self, qnd):
        self.saldo -= qnd
        
obj = ContaCorrente("123456", "Lucas", 1000)
obj.deposito(200)
obj.saque(100)
