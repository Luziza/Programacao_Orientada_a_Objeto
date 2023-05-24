'''• Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago)
e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente,
criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e
verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o
outro. É possível criar um macaco canibal?'''

class Macaco():

  def __init__(self, nome):
    self.nome = nome
    self.bucho = []
  
  def comer(self, comida):
    self.bucho.append(comida)

  def digerir(self):
    if len(self.bucho) > 0 and len(self.bucho) <= 3:
      self.bucho_vazio = self.bucho.clear()
      print(f"{self.bucho_vazio}")
    if len(self.bucho) == 0:
      print(f"o estomago está vazio")
  
  def mostrar(self):
    print(f"{self.bucho}")

macaco1 = Macaco("Laura")
macaco1.comer("maça")
macaco1.mostrar()
macaco1.comer("banana")
macaco1.mostrar()
macaco1.comer("perâ")
macaco1.mostrar()

macaco1.digerir()
