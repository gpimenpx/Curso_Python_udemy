# argparse.ArgumentParser para argumentos mais completos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá Mundo" na tela ',
    # type=str, # Tipo do argumento
    metavar='STRING',
    #default='Olá mundo', # Valor padrão
    required=False,
    action= 'append', # Recebe o argumento mais de uma vez 
    # nargs='+' , # Recebe mais de um valor
    )

parser.add_argument(
    '-v', '--verbose',
    help='Mostra logs',
    action= 'store_true', # Recebe o argumento mais de uma vez 
    )

args = parser.parse_args()
#print(args.b)

if args.basic is None:
    print('Você não passou o valor de b.')
else: 
    print(f'O valor de b {args.basic}')

print(args.verbose)