'''• Classe Pessoa: Crie uma classe que modele uma pessoa:
      a. Atributos: nome, idade, peso e altura
      b. Métodos: envelhercer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos,
ela deve crescer 0,5 cm.'''

class Pessoa():

  def __init__(self, nome, altura, peso, idade):
    self.nome = nome
    self.altura = altura
    self.peso = peso
    self.idade = idade
  
  def envelhecer(self, aumenta):
    self.idade = self.idade + aumenta
  
  def crescer(self):
    if self.idade >= 21:
      self.altura = self.altura + (0.5 * (self.idade - 21))
    else:
      self.altura = self.altura + (0.5 * (21 - self.idade))

  
  def engordar(self, pesoMais):
    self.peso = self.peso + pesoMais
  
  def mostrar(self):
    return f"{self.nome}, {self.altura}, {self.peso}, {self.idade}"

pessoa1 = Pessoa("Luiza", 156, 60, 14)
pessoa1.envelhecer(4)
pessoa1.crescer()
pessoa1.engordar(2)
print(pessoa1.mostrar())
