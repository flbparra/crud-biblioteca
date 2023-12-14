from flask import jsonify, session
from flask_bcrypt import Bcrypt
from service.connectBD import getDB

bcrypt = Bcrypt()

auth = None

def login(data):
    
    global auth
    
    user_login = data.get('Login')
    user_password = data.get('Senha')
    
    conexao = getDB()
    cursor = conexao.cursor(dictionary=True)
    
    cursor.execute(f"SELECT * FROM Usuarios WHERE login = '{user_login}'")
    usuario = cursor.fetchone()
    
    if usuario:
        
        #verifica se a senha é igual a encriptada pelo banco.
        if bcrypt.check_password_hash(usuario['Senha'], user_password):
            
            auth = True
            
            session['usuario_id'] = usuario['ID']
        
            return jsonify({"message" : f"Login realizado com sucesso! Bem vindo {usuario['Funcao']}","id": usuario["ID"]}), 200
    
        else:
            return jsonify({"message" : "Login ou senha incorreto"}), 401

    else:
        return jsonify({"message" : "Usuario não encontrado"}), 400
    
    
    def logoff():
        
        global auth
        auth = None
        
        session.pop('user_id', None)
    
        return jsonify({"message" :"Logout realizado com sucesso"}), 200
    
    
    
    