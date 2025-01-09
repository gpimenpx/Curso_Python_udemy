# Exercício com classes
# 1 - crie uma classe Carro (nome)
# 2 - Crie uma classe Motos()
# 3 - Crie uma classe Fabricante (nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro , motor e fabricante na tela.

class Carro:
    def __init__(self, nome ):
        self.nome = nome
        self._motor =  None
        self._fabricante = None

    @property
    def motor (self):
        return self._motor
        
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante (self):
        return self._fabricante
        
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
    
class Motor:
    def __init__(self, nome ):
        self.nome = nome
        
    
class Fabricante:
    def __init__(self, nome ):
        self.nome=nome
        
fusca = Carro ('Fusca')
volkswagen = Fabricante ('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

gol = Carro ('Gol')
volkswagen = Fabricante ('Volkswagen')
motor_1_0 = Motor('1.0')
gol.fabricante = volkswagen
gol.motor = motor_1_0
print(gol.nome, gol.fabricante.nome, gol.motor.nome)

fiat_uno = Carro ('Uno')
fiat = Fabricante ('Fiat')
motor_1_0 = Motor('1.0')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

focus = Carro ('Focus Titanium 2.')
ford = Fabricante ('Ford')
motor_2_0 = Motor('2.0')
focus.fabricante = ford
focus.motor = motor_2_0
print(focus.nome, focus.fabricante.nome, focus.motor.nome)