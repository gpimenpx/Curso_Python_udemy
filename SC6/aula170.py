# os.listdir para navegar em caminhos
# /Users\guilh/Onedrive/Projeto/SC6  
# "C:\Users\guilh\OneDrive\Projeto\SC6"
# caminho = r'"C:\\Users\\guilh\\OneDrive\\Projeto\\SC6"' "C:\Users\guilh\OneDrive\Imagens\Capturas de tela"
import os

os.system('cls')

caminho = os.path.join('/Users', 'guilh', 'OneDrive', 'Imagens')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    if not os.path.isdir(caminho_completo_pasta):
        continue
    
    for imagem in os.listdir(caminho_completo_pasta):
        print(imagem)