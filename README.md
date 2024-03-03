# Trabalho do Banco de Dados:

[Diagrama do Projeto]((https://github.com/flbparra/Diagrama-BD-Biblioteca))


### Tecnologias Usadas

- __Python__: Instale o python na sua maquina se não o tiver (_logo abaixo tem links que podem a te ajudar a instalar em sua máquina_).

> [Windows](https://www.python.org/downloads/)

> [Linux](https://python.org.br/instalacao-linux/)

- __MYSQL__: Você pode instalar o [MYSQL em seu site oficial](https://dev.mysql.com/downloads/mysql/).

- __VSCode__: Opcional Pode usar qualquer editor de código, porém recomendo usar o [VSCODE](https://code.visualstudio.com/) ou [Pycharm-Community](https://www.jetbrains.com/pt-br/pycharm/).
<br>

- __MYSQL WorkBench__: (Opcional podendo ser qualquer um de sua escolha) SGBD usado para fazer consultas durante os teste e também para criar o DB ([_click aqui para baixar_](https://dev.mysql.com/downloads/workbench/)).

- __[Insomnia](https://docs.insomnia.rest/insomnia/install) / [Postman](https://www.postman.com/downloads/)__: Qualquer um dos dois é uma bom escolha, usando apenas para fazer request com Json para teste. 

#### Bibliotecas e dependências do projeto:
Todas as seguintes bibliotecas foram usadas no projeto e você pode instalar elas direto no terminal, recomendamos que crie um [ambiente virtual](https://docs.python.org/pt-br/3/library/venv.html) para fazer essas instações, se estiver usando Windows como sistema operacional recomendamos também que instale o [Shell Bash](https://www.techtudo.com.br/noticias/2016/04/como-instalar-e-usar-o-shell-bash-do-linux-no-windows-10.ghtml). Logo abaixo vai ter as dependencias do projeto e como instalar elas diretamente pelo terminal (Bash).

- pip: Gerenciador de pacotes do python

Ubuntu ou Shell Bash:
```Bash:
sudo apt-get update
sudo apt-get install python3-pip
```
ArchLinux:
``` Bash:
sudo pacman -Sy python-pip
```

- Flask: Biblioteca do Framework usando para o Back-End do trabalho.
```base:
pip3 install Flask
```
- Flask-Bcrypt: Biblioteca usada para criptografia das senhas dos usuarios.
```bash:
pip3 install Flask-Bcrypt
```

- mysql-connector-python: Biblioteca usada para fazer a conexão com  o banco de dados.
```bash:
pip3 install mysql-connector-python
```

### Funcionamento do CRUD:
Após todas as intalações de dependencias do projeto, podemos testar o CRUD, para isso algumas coisas vão ter que ser feitas, como inciar o banco de dados com o código que está na pasta [sql_scripts](https://github.com/flbparra/db_biblioteca/tree/main/sql_scripts).

Configure também o __connectDB.py__, que está na pasta de [service](https://github.com/flbparra/db_biblioteca/tree/main/biblioteca-DrHerpis/service).

![imagem](/imagens_readme/WhatsApp%20Image%202023-11-30%20at%202.18.57%20PM.jpeg)

Config dessa parte depende do usuario e dos dados que ele passou. No nosso projeto essas acima foram as configurações que usamos para rodar o sistema. Lembre-se sem database, password, port, host e user, o projeto não irar rodar. 

Basta agora configurar o POSTMAN ou Insomnia para rodar as request.

Separamos um tutorial sobre, se não tiver conhcimento sobre o Insomnia ([click aqui](https://blog.cod3r.com.br/testes-de-api-rest-com-o-insomnia/)).

### Documentação das Função em Service:

#### connectDB.py:
- Módulo para estabelecer uma conexão com um banco de dados MySQL.
-  Este módulo fornece uma função `getDB` para estabelecer uma conexão com um banco de dados MySQL. Não recebe nenhum paramento. 
- A função `getDB` retorna um objeto de conexão MySQL quando bem-sucedida ou imprime um erro e encerra o programa em caso de falha.

##### Exemplo de uso:
    from connectDB import getDB

    # Obtendo a conexão com o banco de dados
    conexao_db = getDB()

    # Agora você pode usar `conexao_db` para realizar operações no banco de dados.

### Mudanças que ocorreram durante o trabalho

1 - Inicialmente não iriamos fazer usando Flask, mas sim o Django, porém por pesquisarmos e ver que o Django seria para algo mais robusto, optamos pelo flask, já que é para sistemas mais simples.

2º - Escolhemos também trabalhar com MYSQL WorkBench, por ser um SGBD que se encontra muitos tutoriais e informação sobre ele, então sendo assim descartamos a hipotese de trabalhar com DB-main ou DBeaver.

3º - Para fazer os teste de request, também optamos por fazer usando Insomnia pela facilidade que se tem em usa-lo para fazer as request.


