"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""

import re

# cpf_enviadoUs= '7468248907'\
    # .replace('.','')\
    # .replace(' ','')\
    # .replace('-', '')
entrada=input('CPF[746.824.890-70]: ')
cpf_enviadoUs= re.sub(
    r'[^0-9]',
    '',
    entrada 
)

entrada_e_sequencial=entrada[0]*len(entrada)

nove_digitos=cpf_enviadoUs[:9]
contador_regressivo=10

resultado_digito1=0
for digito1 in nove_digitos:
    resultado_digito1 += int(digito1) * contador_regressivo
    contador_regressivo-=1
digito1=(resultado_digito1 * 10) % 11
digito1=digito1 if digito1<=9 else 0

dez_digitos=nove_digitos+str(digito1)
contador_regressivo_2=11

resultado_digito2=0
for digito in dez_digitos:
    resultado_digito2+=int(digito)*contador_regressivo_2
    contador_regressivo_2-=1
digito2=( resultado_digito2*10 )%11
digito2=digito2 if digito2<= 9 else 0
print(digito2)

cpf_gerado_calculo=f'{nove_digitos}{digito1}{digito02}'

if cpf_enviadoUs== cpf_gerado_calculo:
    print(f'{cpf_enviadoUs} é valido')

else:
    print('Cpf Inválido')