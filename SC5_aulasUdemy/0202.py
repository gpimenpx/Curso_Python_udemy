# Importar Bibliotecas necessárias 
import pandas as pd 
import numpy as np
import zipfile
import requests
from io import BytesIO
import os

# Criar um diretório para armazenar o conteúdo do ENADE
os.makedirs('./enade2019', exist_ok=True)

# Define a URL
url = "https://download.inep.gov.br/microdados/microdados_enade_2019_LGPD.zip"

# Faz Download do conteúdo
filebytes = BytesIO(
    requests.get(url).content 
)

#Extrair o conteúdo do zipfle
myzip = zipfile.ZipFile(filebytes)
myzip.extractall("./enade2019")