# E-Commerce Price Comparison Tool

Este projeto tem como objetivo automatizar a comparação de preços entre diferentes sites de e-commerce.

## Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![UiPath](https://img.shields.io/badge/UiPath-FF6C37?style=for-the-badge&logo=uipath&logoColor=white)
![Power BI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)


## Como funciona

1. Automatização do WebScraping de preços de produtos de múltiplos sites
2. Armazenamento em banco de dados
3. Comparação histórica de preços
4. Alerta de queda de preço por e-mail
5. Exibe os dados no PowerBI

## Como executar o projeto:
    
1. Clone o projeto:
    ```Shel
        git clone https://github.com/JoaoPedro1304/Automatio-E-Comerce-Prices.git
    ```

2. Criar Virtual Enviroent (venv):
    ```Shell
    python -m venv NOME-DA-VENV
    ```
    *No Windows, se python for um comando não reconhecido utilize py:
    ```Shell
        py -m venv NOME-DA-VENV
    ```
    *No linux no caso de não reconhecer python utilize python3: 
    ```Shell
        python3 -m venv NOME-DA-VENV
    ```
3. Comando para ativar a venv:
    Windows:
    ```Shell
        NOME-DA-VENV\Scripts\activate
    ``` 
    ```Shell
        Linux : source NOME-DA-VENV/bin/activate
    ```

4. Instalar dependencias:
    Com a venv ativada instale as dependecias do arquivo requirements.txt
    ```Shell
        pip install -r requirements.txt
    ```

5. Configue variáveis de ambiente:
    Criar um arquivo .env para armazenar as variáveis do banco de dados e outras variáveis de ambiente sensíveis.
    exemplo do .env no arquivo [.env_example](./env_example.txt)

6. Iniciar container do banco de dados:
    Executar docker-compose para subir o container do banco:
    ```Shel
        docker-compose up -d
    ```

