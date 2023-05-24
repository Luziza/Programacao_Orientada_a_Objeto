'''• Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve
ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o
número do canal e o nível do volume permanecem dentro de faixas válidas.'''

class TV():

  def __init__(self, canal, volume):
    self.canal = canal
    self.volume = volume

  def aumentaVol(self, aumenta):
    if self.volume >= aumenta and self.volume <= 100:
      self.volume = self.volume + aumenta
    else: 
      return f"volume já está no máximo"
  
  def diminuiVol(self, diminui):
    if self.volume >= diminui:
      self.volume = self.volume - diminui
    else:
      return f"Já esta no volume minimo"
  
  def __str__(self):
    return f"o canal é {self.canal} e o volume está em {self.volume}"

tv1 = TV(2, 50)
tv1.aumentaVol(50)
#tv1.diminuiVol(60)
print(tv1)
