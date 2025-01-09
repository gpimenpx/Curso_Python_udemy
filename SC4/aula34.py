import importlib

import aula34_m

print(aula34_m.variavel)

for i in range(10):
    importlib.reload(aula34_m)
    print(i)

print('Fim')