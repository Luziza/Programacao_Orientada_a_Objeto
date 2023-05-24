'''• Classe Carro: Implemente uma classe chamada Carro com as seguintes propriedades:
a. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa
quantidade de combustível no tanque.
b. O consumo é especificado no construtor e o nível de combustível inicial é 0.
c. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância,
reduzindo o nível de combustível no tanque de gasolina.
d. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
e. Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
  
meuFusca = Carro(15) # 15 quilômetros por litro de combustível.
meuFusca.adicionarGasolina(20) # abastece com 20 litros de combustível.
meuFusca.andar(100) # anda 100 quilômetros.
meuFusca.obterGasolina() # Imprime o combustível que resta no tanque.'''

class Carro():
  combustivel = 0

  def __init__(self, km_por_litro, km_rodado, mais_combustivel):
    self.km_por_litro = km_por_litro
    self.km_rodado = km_rodado
    self.mais_combustivel = mais_combustivel
  
  def addGasolina(self):
    self.combustivel = self.combustivel + self.mais_combustivel
    print(f"gasolina adicionada {self.combustivel}")

  def andar(self):
    self.combustivel_usado = self.km_rodado / self.km_por_litro
    print(f"o combustivel usado foi {self.combustivel_usado} litros em {self.km_rodado} km")
  
  def obterGasolina(self):
    self.combustivel = self.combustivel - self.combustivel_usado
    print(f"resta {self.combustivel} litros de gasolina no tanque")


carro1 = Carro(10, 20, 50)
carro1.addGasolina()
carro1.andar()
carro1.obterGasolina()
