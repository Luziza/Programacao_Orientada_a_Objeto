'''• Classe Retangulo: Crie uma classe que modele um retangulo:
        a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
        b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
        c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades
        de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e
        de rodapés necessárias para o local.'''


class Retangulo():
  area = ""

  def __init__(self, base, altura):
    self.base = base 
    self.altura = altura

  def calArea(self):
    self.area = self.base * self.altura

  def calPer(self):
    self.per = (self.base * 2) + (self.altura * 2)

  def __str__(self):
    return f" o retângulo tem {self.base}cm de base e {self.altura}cm de altura. A área é de {self.area}cm e o perimetro é de {self.per}cm" 

retangulo1 = Retangulo(10, 5)
retangulo1.calArea()
retangulo1.calPer()
print(retangulo1)
