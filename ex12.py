'''• Classe Conta de Investimento: Faça uma classe chamada contaInvestimento que seja semelhante à
classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um
construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros
(sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma
poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método
adicioneJuros() cinco vezes e imprime o saldo resultante.'''

class contaInvestimento():

  def __init__(self, numeroConta, nome, saldo, juros, tempoMeses):
    self.numeroConta = numeroConta
    self.nome = nome
    self.saldo = saldo
    self.juros = juros
    self.tempoMeses = tempoMeses
  
  

  def adicioneJuros(self):
    n = 0
    while n <= 5:
      self.saldo = self.saldo * (self.juros / 100) * self.tempoMeses
      n += 1
    print(f"seu novo saldo é {self.saldo}")
  
  def __str__(self):
    return f"o numero da conta da {self.nome} é {self.numeroConta}, sua taxa de juros é de {self.juros} e seu saldo vai ser de {self.saldo} em {self.tempoMeses} meses por 5 anos"

conta1 = contaInvestimento(12873879, "Luiza", 1000, 10, 12)
conta1.adicioneJuros()
print(conta1)
