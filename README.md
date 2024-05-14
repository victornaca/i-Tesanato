<h1 p align="center"> 
iTesanato | Challenge Shopper

<h3>Quem sou eu?</h3>
<p align="justify">Olá equipe da Shopper, meu nome é Victor Fernandes. Sou formado em Técnico de TI e atualmente estou no último semestre do curso superior de Tecnólogo em Banco de Dados na FATEC, com previsão de conclusão para julho de 2024.</p>
<p align="justify">Minha paixão por dados começou durante o curso técnico e se desenvolveu enquanto trabalhava como Auxiliar de TI, onde desempenhava diversas funções, incluindo a manipulação de bancos de dados para realizar análises investigativas sobre dados que eventualmente se perdiam no processo. A partir dessa experiência, decidi me dedicar integralmente à área de dados ao ingressar na universidade, absorvendo conceitos, tecnologias e habilidades práticas.</p>
<p align="justify">Tive a oportunidade de atuar como estagiário de Ciência de Dados na EDP, onde pude trabalhar com ferramentas como Databricks e Azure, desenvolvendo scripts ETL e aprofundando meu conhecimento em arquitetura de dados.</p>
<p align="justify">Atualmente, ocupo o cargo de Analista de Dados na Safran, onde estou ajudando a desenvolver uma nova equipe de dados no Brasil. Estamos buscando tecnologias internas de outras unidades para criar uma estrutura de data lake para a equipe e iniciar projetos com inteligência artificial.</p>
<p align="justify">Espero que apreciem os resultados do desafio. Estou extremamente satisfeito com ele. Até breve em nossas futuras conversas! :)</p>

<h3>Instalação</h3>
# Como instalar as dependências usando o requirements.txt

Este projeto utiliza um arquivo `requirements.txt` para listar todas as bibliotecas Python necessárias para serem instaladas.

1. Certifique-se de ter o Python instalado em seu sistema. Se ainda não o tiver, você pode baixá-lo em [python.org](https://www.python.org/downloads/).

2. Abra um terminal ou prompt de comando.

3. Navegue até o diretório do projeto onde está localizado o arquivo `requirements.txt`. Você pode usar o comando `cd` (change directory) para isso. Por exemplo:
    ```bash
    cd caminho/para/diretorio/do/projeto
    ```

4. Após navegar até o diretório do projeto, você pode usar o comando `pip` para instalar todas as dependências listadas no arquivo `requirements.txt`. Execute o seguinte comando:
    ```bash
    pip install -r requirements.txt
    ```

Isso instalará todas as bibliotecas listadas no arquivo `requirements.txt` e suas dependências correspondentes.

<h3>Executar Aplicação</h3>
Para executar o projeto, você precisará seguir estas etapas:

1. **Executar o servidor da API:**

   Abra um terminal ou prompt de comando e navegue até o diretório do projeto onde está localizado o arquivo `run_api_server.py`. Em seguida, execute o seguinte comando:
   ```bash
   python run_api_server.py
   ```

2. **Executar o projeto:**

    Em outro terminal ou prompt execute o `app.py`. Não esqueça que o run_api_server.py e o app.py tem que ser executado em paralelo, ambos juntos.
    ```bash
   python app.py
   ```

Os processos de orquestrador começam a rodar depois de 30s, depois só olhar a mágica acontecer :)