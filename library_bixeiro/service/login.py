from flask import jsonify
from flask_bcrypt import Bcrypt
from service.connectBD import getDB

bcrypt = Bcrypt()

def render_login(data):
    
    user_login = data.get('Login')
    user_password = data.get('Senha')
    
    conexao = getDB()
    cursor = conexao.cursor(dictionary=True)
    
    cursor.execute(f"SELECT * FROM Usuarios WHERE login = '{user_login}'")
    usuario = cursor.fetchone()
    
    if usuario:
        
        #verifica se a senha é igual a encriptada pelo banco.
        if bcrypt.check_password_hash(usuario['Senha'], user_password):
        
            return jsonify({"message" : f"Login realizado com sucesso! Bem vindo {usuario['Funcao']}"}), 200
    
        else:
            return jsonify({"message" : "Login ou senha incorreto"}), 401

    else:
        return jsonify({"message" : "Usuario não encontrado"}), 404