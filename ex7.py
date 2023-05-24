'''• Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
a. Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade;
Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar
em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os
atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo
para armazenar esta informação por que ela pode ser calculada a qualquer momento.'''

class Tamagushi():

  def __init__(self, nome, saude, idade, fome):
    self.nome = nome
    self.saude = saude
    self.idade = idade
    self.fome = fome

  def __str__(self):
    return f"{self.nome}, {self.saude}, {self.idade}, {self.fome}"

  def humor(self):
    if self.saude >= 50 and self.fome >= 50:
      print(self.nome + " está muito feliz")
    elif self.saude >= 50 or self.fome >= 50:
      print(self.nome + " está um pouco tristinho")
    else:
      print(self.nome + " está triste")
  
  def __str__(self):
    return f"{self.nome}, tem {self.idade} anos, está com {self.saude} pontos na barra de saúde e {self.fome} pontos na barra de fome"

bixo1 = Tamagushi("Kenan Jr", 30, 47, 10)
bixo1.humor()
print(bixo1)
