'''• Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
i. tipoCombustivel.
ii. valorLitro
iii. quantidadeCombustivel
b. Possua no mínimo esses métodos:
i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a
quantidade de litros que foi colocada no veículo
ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de
combustível e mostra o valor a ser pago pelo cliente.
iii. alterarValor( ) – altera o valor do litro do combustível.
iv. alterarCombustivel( ) – altera o tipo do combustível.
v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na
bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de
combustível total na bomba.'''

class BombaCombust():

  def __init__(self, tipo, valorLitro, quantidadeC):
    self.tipo = tipo
    self.valorLitro = valorLitro
    self.quantidadeC = quantidadeC

  def __str__(self):
    return f"na bomba nós temos {self.quantidadeC} do tipo de gasolina {self.tipo}, no valor de {self.valorLitro} reais"
  
  def abastecerPorValor(self, valorColocado):
    self.abastecidoV = valorColocado / self.valorLitro
    self.quantidadeC = self.quantidadeC + self.abastecidoV
    print(f"foi abastecido {self.abastecidoV} litros então agora temos {self.quantidadeC} de litros na bomba")
  
  def abastecerPorLitro(self, quantidadeColocada):
    self.abastecidoQ = quantidadeColocada * self.valorLitro
    self.quantidadeC = self.quantidadeC + quantidadeColocada
    print(f"foi abastecido {quantidadeColocada} litros e usado {self.abastecidoQ} reais, então agora temos {self.quantidadeC}")
  


carro1 = BombaCombust("diesel", 4, 10)
carro1.abastecerPorValor(10)
carro1.abastecerPorLitro(20)
print(carro1)
