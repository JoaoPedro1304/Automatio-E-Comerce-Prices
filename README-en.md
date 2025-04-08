# E-Commerce Price Comparison Tool

This project aims to automate price comparison across different e-commerce websites.

## Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)  
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)  
![UiPath](https://img.shields.io/badge/UiPath-FF6C37?style=for-the-badge&logo=uipath&logoColor=white)  
![Power BI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)  
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

## How It Works

1. Scraping product prices from multiple websites  
2. Storing the data in a database  
3. Comparing historical prices  
4. Sending price drop alerts via email

## How to Run the Project

### 1. Clone the Repository
    ```shell
        git clone https://github.com/JoaoPedro1304/Automatio-E-Comerce-Prices.git
    ```
2. Create a Virtual Environment (venv)
    ```shell
        python -m venv YOUR-VENV-NAME
    ```
    On Windows, if python is not recognized, use:
    ```shell
        py -m venv YOUR-VENV-NAME
    ```
    On Linux, if python is not recognized, use:
    ```shell
        python3 -m venv YOUR-VENV-NAME
    ```

3. Activate the Virtual Environment
    Windows:
    ```shell
        YOUR-VENV-NAME\Scripts\activate
    ```
    Linux:
    ```shell
        source YOUR-VENV-NAME/bin/activate
    ```

4. Install Dependencies
    With the virtual environment activated, install the required packages:
    ```shell
        pip install -r requirements.txt
    ```
5. Configure Environment Variables:
    Create a .env file to store database credentials and other sensitive settings.
    Use the example file as a reference: [.env_example](./env_example.txt)

6. Start the Database Container
    Run Docker Compose to spin up the PostgreSQL container:
    ```shell
        docker-compose up -d
    ```

