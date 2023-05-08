## 1.Escreva a classe Usuario e adicione as propriedades e o método (em Python):

class Usuario:
  nome = input('Escreva seu nome ')
  sobrenome = input('Escreva seu sobrenome ')

  def hello(self):
    return " Olá!"

## 2.Crie a primeira instância e chame-a de usuario1:

class Usuario:
  nome = input('Escreva seu nome ')
  sobrenome = input('Escreva seu sobrenome ')

  def hello(self):
    return " Olá!"

usuario1 = Usuario()

## 3.Defina os valores do primeiro e último nome para usuario1:

class Usuario:
  nome = ''
  sobrenome = ''

  def hello(self):
    return " Olá!"

usuario1.nome = 'Luiza '
usuario1.sobrenome = 'Ribeiro'

## 4.Obter o nome e sobrenome do usuário e imprima-os na tela com o comando print.

class Usuario:
  nome = input('Escreva seu nome ')
  sobrenome = input('Escreva seu sobrenome ')

  def hello(self):
    return " Olá!"

usuario1 = Usuario()

print(usuario1.nome + ' ' + usuario1.sobrenome)

## 5. Use o método que retorna “Olá” com as variáveis primeiro nome e último nome para dizer Olá ao usuário:

class Usuario:
  nome = input('Escreva seu nome ')
  sobrenome = input('Escreva seu sobrenome ')

  def hello(self):
    return " Olá!"
  
usuario1 = Usuario()
  
print(usuario1.nome + usuario1.sobrenome + usuario1.hello())

## 6. Crie (instancie) outro objeto. Chame-o de usuario2, dê a ele o primeiro nome de “Jane” e o sobrenome de “Silva”, e depois diga “Olá” ao usuário:

class Usuario:
  nome = ''
  sobrenome = '' 

  def hello(self):
    return " Olá!"
  
usuario1 = Usuario()
usuario2 = Usuario()

usuario2.nome = 'Jane '
usuario2.sobrenome = 'Silva'
  
print(usuario2.nome + usuario2.sobrenome + usuario2.hello())

