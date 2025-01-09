# Exercício
# Crie funções que duplicam , triplicam e quadruplicam o número recebido como parâmetr

# def duplicar(numero):
#     return numero *2
# def triplicar(numero):
#     return numero*3
# def quadru(numero):
#     return numero*4

# print(duplicar(2))
# print(triplicar(2))
# print(quadru(20))

def criar_multriplicador(multiplicador):
    def multiplicar(numero):
        return numero*multiplicador
    return multiplicar

duplicar=criar_multriplicador(2)
triplicar=criar_multriplicador(3)
quadruplicar=criar_multriplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))