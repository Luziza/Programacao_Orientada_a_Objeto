'''• Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e
um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para
devolver nome e salário. Escreva um pequeno programa que teste sua classe.'''

class Funcionario():

    def __init__(self, nome, salario):
      self.nome = nome
      self.salario = salario
    
    def aumento(self, porcentagem):
      self.salario_novo = self.salario + ((self.salario * porcentagem) / 100)
      print(f"o novo salário é {self.salario_novo} com {porcentagem}% de aumento")
    
    def __str__(self):
      return f"o nome do funcionario é {self.nome} e seu salario é de {self.salario}"

funcionario1 = Funcionario("Luiza", 1000)
funcionario1.aumento(10)
print(funcionario1)
