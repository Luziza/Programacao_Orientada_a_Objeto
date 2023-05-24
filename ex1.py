'''• Classe Bola: Crie uma classe que modele uma bola:
      a. Atributos: Cor, circunferência, material
      b. Métodos: trocaCor e mostraCor '''
      
class Bola():
  cor = ""
  circunferencia = ""
  material = ""

  def trocaCor(self, cor):
    self.cor = cor

  def mostraCor(self):
    return "a bola é da cor " + self.cor
  
bola1 = Bola()
bola1.trocaCor("preto")

print(bola1.mostraCor())
