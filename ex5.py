'''• Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve
possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os
seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os
demais atributos são obrigatórios.'''

class ContaCorrente():

  def __init__(self, numeroConta, nome, saldo):
    self.numeroConta = numeroConta
    self.nome = nome
    self.saldo = saldo
  
  def __str__(self):
    return f"o numero da conta da {self.nome} é {self.numeroConta} e seu saldo inicial é de {self.saldo}"

  def deposito(self, valorD):
    self.saldo1 = self.saldo + valorD
    print(f"o depósito foi de {valorD} e o seu saldo agora é de {self.saldo1}")

  def saque(self, valorS):
    self.saldo1 = self.saldo1 - valorS
    print(f"o saque foi de {valorS} e o seu saldo agora é de {self.saldo1}")

conta1 = ContaCorrente(1231234, "Luiza", 1200)
conta1.deposito(300)
conta1.saque(400)
print(conta1)
