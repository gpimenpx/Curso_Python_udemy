# Exercícios com funções

# Crie uma função que multiplica todos or agrgumentos não nomeados recebidos
#Retorone o total para um varivavel e mostre o valor da variável  na tela 

def multilpicar (*args):
    total=1
    for numero in args:
        total *=numero
    return total

multiplicacao=multilpicar(10, 2, 3, 4, 5)
print(multiplicacao)
# Crie uma funcçãoque sala se um numero é par ou ímpar.
#Retorne se o número é par ou impar .

def par_impar(numero):
    multiplo_de_dois= numero % 2 ==0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'

print(par_impar(2))
print(par_impar(3))
print(par_impar(15))