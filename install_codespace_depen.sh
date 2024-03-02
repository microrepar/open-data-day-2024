#!/bin/bash

# Instala o gerenciador de instalação pipx
python3 -m pip install -U pipx

# Instala o gerenciador de dependências em projetos Python, o Poetry
pipx install poetry

# Verifica se a instalação do Poetry foi bem-sucedida
poetry --version

# Criação do ambiente virtual e instalação das dependências do projeto
poetry install

# Baixa os binários da versão mais recente do Google Chrome
wget https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/linux64/chrome-linux64.zip

# Aguarda o download ser concluído
while [ ! -f chrome-linux64.zip ]; do
    sleep 1
done

# Descompacta o arquivo chrome-linux64.zip
unzip chrome-linux64.zip

while [ ! -d chrome-linux64 ]; do
    sleep 1
done

# Move o diretório descompactado para /opt/google/chrome
sudo mkdir /opt/google
sudo mv chrome-linux64 /opt/google/chrome

# Cria um link simbólico para o binário do Chrome em /usr/bin/
sudo ln -s /opt/google/chrome/chrome /usr/bin/google-chrome

sudo cp .env-exemplo .env
