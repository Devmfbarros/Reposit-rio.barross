#1. Defina classes
Uma classe é um tipo de estrutura de dados que define as características e
comportamentos de um objeto. Ela é uma espécie de molde a partir do qual os objetos
podem ser criados. Em linguagens de programação orientada a objetos, como Python ou
Java, as classes são fundamentais para organizar e estruturar o código.


#2. Defina métodos
Um método é uma função definida dentro de uma classe que descreve o
comportamento dos objetos dessa classe. Métodos podem acessar e modificar os atributos
da classe e podem interagir com outros objetos.


#3. Defina funções
Uma função é um bloco de código que realiza uma tarefa específica e pode
retornar um valor. Em contraste com os métodos, as funções não estão associadas a uma
classe específica.


#4 Pesquise um exemplo de função

def fibonacci_sequence(n):
sequence = [0, 1]
while len(sequence) < n:
next_term = sequence[-1] + sequence[-2]
sequence.append(next_term)
return sequence



#5 Explique o funcionamento da questão

Esta função recebe um número `n` como entrada e retorna uma lista com os primeiros `n`
termos da sequência de Fibonacci. Ela começa com os dois primeiros termos da sequência
(0 e 1) e, em seguida, calcula os próximos termos adicionando os dois últimos termos
calculados à lista até que a lista tenha `n` elementos.


#6. PESQUISE 1 EXEMPLO DE CRIAÇÃO DE CLASSE COM MAIS DE 1O LINMAS

class Car:
def __init__(self, brand, model, year, color):
self.brand = brand
self.model = model
self.year = year
self.color = color
self.mileage = 0
self.engine_status = 'off'
def start_engine(self):
self.engine_status = 'on'
def stop_engine(self):
self.engine_status = 'off'
def drive(self, distance):
if self.engine_status == 'on':
self.mileage += distance
print(f"{self.brand} {self.model} has driven {distance} miles.")
else:
print("Cannot drive. Engine is off.")



#7. EXPLIQUE O FUNCIONAMENTO DA CLASSE.

Esta classe `Car` define as características e comportamentos de um carro. Ela possui
atributos como marca, modelo, ano, cor, quilometragem e status do motor, e métodos para
ligar o motor, desligar o motor e dirigir o carro.


#8. QUAIS SEUS ATRIBUTOS?

 `brand`: marca do carro
 `model`: modelo do carro
 `year`: ano do carro
 `color`: cor do carro
 `mileage`: quilometragem do carro
 `engine_status`: status do motor do carro ('on' ou 'off')


#9. QUAIS SEUS MÉTODOS?

 `__init__`: inicializa os atributos do carro
 `start_engine`: liga o motor do carro
 `stop_engine`: desliga o motor do carro
 `drive`: simula a ação de dirigir o carro, aumentando a quilometragem se o motor estiver
ligado.


#10. CITE E EXPLIQUE OS PRINCIPAIS TIPOS DE DADOS

 **Inteiro (int):** Representa números inteiros, como -3, 0, 42.
 **Flutuante (float):** Representa números decimais, como 3.14, -0.001, 2.0.
 **String (str):** Sequência de caracteres, como "hello", "world", "Python".
 **Booleano (bool):** Representa valores verdadeiro ou falso, True ou False.
 **Lista (list):** Coleção ordenada de itens, mutável e pode conter elementos de
diferentes tipos.
- **Dicionário (dict):** Coleção de pares chave-valor, onde cada chave é única e
associada a um valor.
 **Tupla (tuple):** Coleção ordenada e imutável de elementos, semelhante a uma lista,
mas seus elementos não podem ser alterados após a criação.
 **Conjunto (set):** Coleção desordenada de elementos únicos, não permite elementos
duplicados.
