'''• Classe Quadrado: Crie uma classe que modele um quadrado:
      a. Atributos: Tamanho do lado
      b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;'''

class Quadrado():
  tamanho_lado = ""

  def trocaLado(self, tamanho_lado):
    self.tamanho_lado = tamanho_lado

  def calcQuadrado(self):
    self.area = self.tamanho_lado * self.tamanho_lado
  
  def __str__(self):
    return f"o quadrado tem {self.tamanho_lado} lados e {self.area} de área"

quadrado1 = Quadrado()
quadrado1.trocaLado(5)
quadrado1.calcQuadrado()
print(quadrado1) 
