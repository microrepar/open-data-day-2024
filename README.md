# Open Data Day - 2024 
## Oficina
## Descrição

Oficina de dados para coleta e tratamento dos recursos disponíveis, em valores, a serem distribuídos entre os Objetivos de Desenvolvimento Sustentáveis (ODS). Criação de dashboard com a linguagem de programação python e publicação do app na Cloud.

## Hands-On
 - Criação de ambiente de desenvolvimento nas Nuvens.

 - Construção de um dashboard com Python.

 - Publicação do dashboard em um servidor Cloud.

## Pré-requisitos

Serão necessários as seguintes ferramentas para execução do projeto:
 - **Visual Studio Code (VS Code)**  - é um editor de código-fonte desenvolvido pela Microsoft para Windows, Linux e macOS. Ele inclui suporte para depuração, controle de versionamento Git incorporado, realce de sintaxe, complementação inteligente de código, snippets e refatoração de código. Além disso, é customizável, permitindo que os usuários possam mudar o tema do editor e teclas de atalho de suas preferências.

 - **Python 3.11** - é uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. É frequentemente usada para desenvolvimento web, análise de dados, aprendizado de máquina, inteligência artificial, computação científica, entre outros. É conhecida por sua sintaxe clara e legível.

 - **pipx** -  é uma ferramenta que facilita a instalação de aplicativos Python isolados, usando o PyPI como índice de pacotes. Ele é semelhante ao pip, que é um instalador de pacotes Python para bibliotecas e aplicativos. No entanto, o pipx é feito especificamente para aplicativos, criando um ambiente isolado para cada aplicativo e suas dependências.
 
 - **Poetry** - é uma ferramenta para gerenciar dependências em projetos Python. Ele simplifica o gerenciamento de dependências e garante a reprodutibilidade do ambiente de desenvolvimento. Com o Poetry, é fácil adicionar, atualizar e remover dependências, bem como criar e gerenciar ambientes virtuais de desenvolvimento.

 - **Git** - é um sistema de controle de versão moderno e amplamente utilizado, desenvolvido em 2005 por Linus Torvalds, o famoso criador do kernel do sistema operacional Linux. Ele é usado para controlar o histórico de alterações de arquivos, principalmente de projetos de desenvolvimento de software.

 - **GitHub** - é uma plataforma de hospedagem de código-fonte que utiliza o sistema de controle de versão Git. Ele permite que programadores, utilitários ou qualquer usuário cadastrado na plataforma contribuam em projetos privados e/ou de código aberto de qualquer lugar do mundo.

## Instalação
A instalação deverá ser executada na seguinte ordem:
 1. Vscode - [Página de download aqui](https://code.visualstudio.com/download)

 2. Python - [Página de download aqui](https://www.python.org/)

 3. pipx - [Página de download aqui](https://packaging.python.org/pt-br/latest/guides/installing-stand-alone-command-line-tools/)

 4. Poetry - [Página de download aqui](https://python-poetry.org/docs/#installation)

 5. Git - [Página de download aqui](https://git-scm.com/downloads)

## Executar o projeto no pc
 1. Após configurado o ambiente e efetuado a instalação, agora é preciso fazer o clone do projeto no repositório remoto do GitHub.
    ```bash
    git clone [endereco_do_repositorio]
    ```

 2. Instale as dependências do projeto executando o comando a seguir, com o terminal aberto na raiz do projeto.
    ```bash
    poetry install
    ```

 3. Ative o ambiente virtual no qual foi instalado as dependências com o seguinte comando:
    ```bash
    poetry shell
    ```

 4. Após ativo o ambiente virtual, execute a aplicação streamlit.
    ```bash
    streamlit run streamlit_app.py
    ```

    Em seguida irá abrir o browser com a aplicação em execução.


## Executar o projeto no Codespaces - GitHub
 1. Faça um fork no GitHub do projeto `https://github.com/microrepar/open-data-day-2024`

 2. Crie um Codespaces do projeto que foi efetuado o fork.

 3. Altere o nome do arquivo `.env-exemplo` para `.env`.

 4. Instale o gerenciador de intalação `pipx`:
    ```bash
    python3 -m pip install -U pipx
    ```

 5. Instale o gerenciador de dependências em projetos python `poetry`:
    ```bash
    pipx install poetry
    ```

    Verifique se a instalação foi bem sussedida `poetry --version`.

 6. Efetue criação do ambiente virtual e a instalação das dependências do projeto executando o comando seguir:
    ```bash
    poetry install
    ```

 7. Ative o ambiente virtual que foi construído com o comando anterior.
    ```bash
    poetry shell
    ```    

    Se tudo correu bem, no inicio do prompt de comando, será exibido entre parenteses o nome do ambiente virtual ativo.

 8. Após ativo o ambiente virtual, execute a aplicação streamlit.
    ```bash
    streamlit run streamlit_app.py
    ```
    
    Obs.: Na caixa de diálogo que será aberta, confirme para "**abrir no navegador**".

    Em seguida irá abrir o browser com a aplicação em execução.

## Conteúdo Extra
### Executar o selenium no Codespaces
1. Efetue a instalacao do google-chrome via terminal
    - Acesse o site em https://googlechromelabs.github.io/chrome-for-testing/ e copie o link da última versão do browser.
    - Baixe os binários:
       ```bash
       sudo wget [url_do_binário]
       ```
    - Descompacte o arquivo .zip:
       ```bash
       unzip [nome_do_arquivo.zip]
       ```
    - Crie o diretório `/opt/google/`.
       ```bash
       sudo mkdir /opt/google
       ```
    - Mova o diretório descompactado para `/opt/google/chrome`.
       ```bash
       sudo mv [diretorio_descompactado] /opt/google/chrome
       ```
    - Crie um link simbólico para o binário do chrome e adicione em '/usr/bin/'.
       ```bash
       sudo ln -s /opt/google/chrome/chrome /usr/bin/google-chrome
       ```

2. Subistitua os options de configuração do webdriver, no arquivo `open_data_day_2024/web_page.py`, pelo trecho de código a seguir.
   ```python
   ...
       options = Options()
       options.add_argument("--headless")
       options.add_argument("--no-sandbox")
   ...
   ```

3. Altere o nome do arquivo `.env-exemplo` para `.env`.

4. Abra o notebook `coleta_tratamento_dados.ipynb` e selecione o kernel (interpretador python do ambiente virtual).
    - Selecione a opção `instalar/habilitar extensões sugeridas`.
    - Em seguida selecione a opção `Python Environments...`

5. Execute todo o notebook jupyter clicando no botão `>> Executar Tudo`.

### Arquivo de configuração do VsCode `settings.json`
```json
{
    "material-icon-theme.folders.associations": {
        "core": "rules",
        "adapters": "pipe",
        "external": "tools",
        "pages": "rules",
        "user": "admin",
        "notebook": "lib",
        "pagesection": "lib",
        "sentence": "lib",
        "alembic": "config",
        ".streamlit": "config",
        ".documentation": "resource",
        "persistence": "database",
        "meu_app": "app",    
        "open_data_day_2024": "app"       
    },
    "files.exclude": {
        "**/*.pyc": {"when": "$(basename).py"},
        "**/__pycache__": true,
        "**/*.pytest_cache": true,
    }
}
```
## Links úteis
 - https://www.python.org/
 - https://pypi.org/
 - https://github.com/pypa/pipx
 - https://python-poetry.org/
 - https://docs.streamlit.io/
 - https://plotly.com/python/
 - https://www.selenium.dev/
 - https://googlechromelabs.github.io/chrome-for-testing/
 - https://www.w3schools.com/xml/xpath_intro.asp
 - https://developer.mozilla.org/en-US/docs/Web/XPath
 - https://docs.github.com/pt/codespaces
 - https://git-scm.com/docs
 - https://git-scm.com/book/pt-br/v2

## Licença
MIT license
