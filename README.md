# Open Data Day 2024 - Oficina de Dados

## Descrição

Coleta e tratamento dos recursos (em valores) disponíveis  para os ODS e criação de dashbords com a linguagem de programação python.

## Pré-requisitos

Serão necessários as seguintes ferramentas para execução do projeto:
 - **Visual Studio Code (VS Code)**  - é um editor de código-fonte desenvolvido pela Microsoft para Windows, Linux e macOS1. Ele inclui suporte para depuração, controle de versionamento Git incorporado, realce de sintaxe, complementação inteligente de código, snippets e refatoração de código1. Além disso, é customizável, permitindo que os usuários possam mudar o tema do editor, teclas de atalho e preferências. O VS Code é um software de código aberto

 - **Python 3.11** - é uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. É frequentemente usada para desenvolvimento web, análise de dados, aprendizado de máquina, inteligência artificial, computação científica, entre outros. É conhecida por sua sintaxe clara e legível.

 - **pipx** -  é uma ferramenta que facilita a instalação de aplicativos Python isolados, usando o PyPI como índice de pacotes. Ele é semelhante ao pip, que é um instalador de pacotes Python para bibliotecas e aplicativos. No entanto, o pipx é feito especificamente para aplicativos, criando um ambiente isolado para cada aplicativo e suas dependências.
 
 - **Poetry** - é uma ferramenta para gerenciar dependências em projetos Python. Ele simplifica o gerenciamento de dependências e garante a reprodutibilidade do ambiente de desenvolvimento. Com o Poetry, é fácil adicionar, atualizar e remover dependências, bem como criar e gerenciar ambientes virtuais de desenvolvimento.

## Instalação
A instalação deverá ser executada na seguinte ordem:
 1. Vscode - [Página de download aqui](https://code.visualstudio.com/download)
 2. Python - [Página de download aqui](https://www.python.org/)
 3. pipx - [Página de download aqui](https://packaging.python.org/pt-br/latest/guides/installing-stand-alone-command-line-tools/)
 4. Poetry - [Página de download aqui](https://python-poetry.org/docs/#installation)

## Executar o projeto no pc
 1. Após configurado o ambiente e efetuado a instalação, agora é preciso fazer o clone do projeto no repositório remoto do GitHub:
    ```bash
    git clone [endereco_do_repositorio]
    ```
 2. Instale as dependências do projeto executando o comando seguir, com o terminal aberto na raiz do projeto:
    ```bash
    poetry install
    ```
 3. Ative o ambiente virtual no qual foi instalado as dependências com o comando a seguir:
    ```bash
    poetry shell
    ```
 4. Após ativo o ambiente virtual, execute a aplicação streamlit
    ```bash
    streamlit run streamlit_app.py
    ```
    Em seguida irá abrir o browser com a aplicação em execução.


## Executar o projeto no CodeSpace - GitHub
1. Faça um fork no GitHub do projeto.
2. Crie um Codespace do projeto que foi efetuado o fork.
3. Altere o nome do arquivo `.env-exemplo` para `.env`.
4. Instale o gerenciador de intalação `pipx`:
    ```bash
    $ python3 -m pip install -U pipx
    ```
5. Instale o gerenciador de dependências em projetos python `poetry`:
    ```bash
    $ pipx install poetry
    ```
    Verifique se a instalação foi bem sussedida `$ poetry --version`

6. Efetue criação do ambiente virtual e a instalação das dependências do projeto executando o comando seguir:
    ```bash
    $ poetry install
    ```
7. Ative o ambiente virtual que foi construído com o comando anterior.
    ```bash
    $ poetry shell
    ```    
    Se tudo correu bem, no inicio do prompt de comando, será exibido entre parenteses o nome do ambiente virtual ativo.

8. Após ativo o ambiente virtual, execute a aplicação streamlit.
    ```bash
    $ streamlit run streamlit_app.py
    ```

    Em seguida irá abrir o browser com a aplicação em execução.

    obs.: Confirmar na caixa de diálogo para abrir no navegador.

## Conteúdo Extra
### Executar o selenium no CodeSpace
1. Efetue a instalacao do google-chrome via terminal
 - Acesse o site em https://googlechromelabs.github.io/chrome-for-testing/ e copie o link da última versão do browser.
 - Baixe os binários:
    ```bash
    $ sudo wget [url_do_binário]
    ```
 - Descompacte o arquivo .zip:
    ```bash
    $ unzip [nome_do_arquivo.zip]
    ```
 - Crie o diretório `/opt/google/`.
    ```bash
    $ sudo mkdir /opt/google
    ```
 - Mova o diretório descompactado para `/opt/google/chrome`.
    ```bash
    $ sudo mv [diretorio_descompactado] /opt/google/chrome
    ```
 - Crie um link simbólico para o binário do chrome e adicione em '/usr/bin/'.
    ```bash
    $ sudo ln -s /opt/google/chrome/chrome /usr/bin/google-chrome
    ```
2. Abra o notebook `coleta_tratamento_dados.ipynb` e selecione o kernel (interpretador python do ambiente virtual).
3. Altere os options de configuração do webdriver, no arquivo `web_page.py`, pelo trecho a seguir.
    ```python
    ...
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
    ...
    ```
 4. Altere o nome do arquivo `.env-exemplo` para `.env`.
 5. Execute todo o notebook jupyter clicando no botão `>> Executar Tudo`

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

## Licença
MIT license
