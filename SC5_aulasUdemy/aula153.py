# Método especial __call__
# Callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma 
# Classe "Callable"



class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome,'Está Chamando', self.phone)


call1= CallMe('+55 (11) 98512-8023')
call1('Guilherme')