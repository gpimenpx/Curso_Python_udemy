"""Calculadora com While """

# numero=input('Digite um numero: ')
# numero2=input('Digite outro numero: ')
# print('Aguarde...')

# qtd_numero=0
# qtd_numero2=0

# while qtd_numero < numero==10:
#     qtd_numero=numero*numero2
#     print(qtd_numero)
#     qtd_numero+=1


while True:
    numero_1=input('Digite um numero : ')
    numero_2=input('Digite outro numero :')
    operador=input('Digite um operador (+-/*): ')

    numeros_validos=None
    num_1_float=0
    num_2_float=0

    try:
        num_1_float=float(numero_1)
        num_2_float=float(numero_2)
        numeros_validos=True

    except:
        numeros_validos=None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são invalidos')
        continue

    operadores_permitidos='+-/*'

    if operador not in operadores_permitidos: 
        print('Operador inválido')
        continue

    if len(operador)>1:
        print('Digite apenas um operador.')
        continue
        
    print('Realizando sua conta, confira o resultado abaixo: ')
    if operador=='+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float+num_2_float)
    elif operador=='-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float-num_2_float)
    elif operador=='/':
        print(f'{num_1_float}/{num_2_float}=', num_1_float/num_2_float)
    elif operador=='*':
        print(f'{num_1_float}*{num_2_float}=', num_1_float*num_2_float)
    
    else:
        ('nunca deveria chegar aqui')

    sair=input('Quer sair ? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break