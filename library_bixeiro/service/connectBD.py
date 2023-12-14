import mysql.connector
import sys

# Configuração do banco de dados

def getDB():
    try:
        db_conexao = mysql.connector.connect(
            host='127.0.0.1',   
            port= '3306',
            user='root',
            password='br4b0@',
            database='ame',
        )
        
        return db_conexao
    
    except mysql.connector.Error as erro:
        print(f'Erro connection com o BANCO DE DADOS: {erro}')
        sys.exit(1)
