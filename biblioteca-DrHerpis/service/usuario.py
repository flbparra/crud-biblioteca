from service.connectBD import getDB
from flask_bcrypt import Bcrypt
from flask import request, json, jsonify

bcrypt = Bcrypt()



def create_new_user(ID, Nome, Sobrenome, Funcao, Login, Senha, URIFotoUsuario):
    
    conexao = getDB()
    cursor = conexao.cursor()
    senha_crypt = bcrypt.generate_password_hash(Senha).decode('utf-8')
    
    query = "INSERT INTO Usuarios(ID, Nome, Sobrenome, Funcao, Login, Senha, URIFotoUsuario) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    
    
    cursor.execute(query, (ID, Nome, Sobrenome, Funcao, Login, senha_crypt, URIFotoUsuario))
    conexao.commit()
    
    
    usuario_cadastrado = get_user_id(ID)
    usuario_cadastrado = usuario_cadastrado.get_json()
    
    conexao.close()
    
    return jsonify({"mensage" : "Usuario cadastrado com sucesso", "Usuario" : usuario_cadastrado }), 200


def get_user_id(ID):
    
    conexao = getDB()
    cursor = conexao.cursor()
    
    cursor.execute(f"SELECT ID, Nome, Sobrenome, Funcao, URIFotoUsuario FROM Usuarios WHERE ID = {ID}")
    
    infoUsuario= []
    
    for row in cursor:
        ID, Nome, Sobrenome, Funcao, URIFotoUsuario = row 
        infoUsuario.append(
            {
                "ID" : ID,
                "Nome" : Nome,
                "Sobrenome" : Sobrenome,
                "Funcao" : Funcao,
                "URIFotoUsuario" : URIFotoUsuario
            }
        )   
    conexao.close()
    
    return jsonify(infoUsuario)


def get_all_users():
    
    conexao = getDB()
    cursor = conexao.cursor()

    cursor.execute("SELECT ID, Nome, Sobrenome, Funcao, URIFotoUsuario FROM Usuarios")
    
    allUser = []
    
    for row in cursor:
        ID, Nome, Sobrenome, Funcao, URIFotoUsuario = row
        
        allUser.append(
            {
                "ID" : ID,
                "Nome" : Nome,
                "Sobrenome" : Sobrenome,
                "Funcao" : Funcao,
                "URIFotoUsuario" : URIFotoUsuario
            }
        )        
    
    conexao.close()
    return jsonify({
        "Usuarios cadastrados no Sistema" : allUser
    })
    
def update_user(ID):
    conexao = getDB()
    cursor = conexao.cursor()
    
    cursor.execute(f"SELECT ID FROM Usuarios WHERE ID = {ID}")
    usuario_exite = cursor.fetchone()
    
    if not usuario_exite:
        conexao.close()
        return jsonify({"message" : "Usuario não encontrado"}), 404
        
    usuario_data = request.json
    
    query = "UPDATE Usuarios SET Nome=%s, Sobrenome=%s, Funcao=%s, URIFotoUsuario=%s WHERE ID=%s"
    
    cursor.execute(query,(usuario_data.get('Nome'),
            usuario_data.get('Sobrenome'),
            usuario_data.get('Funcao'),
            usuario_data.get('URIFotoUsuario'),
            ID))
    
    conexao.commit()
    conexao.close()
    
    return jsonify({"message" : "Usuario atualizado com suscesso"})



def delete_user(ID):
    conexao = getDB()
    cursor = conexao.cursor()
    
    try:
        
        cursor.execute(f"SELECT ID FROM Usuarios WHERE ID = {ID}")
        usuario_exite = cursor.fetchone()
        
        if not usuario_exite:
            return jsonify({"message" : "Usuario não encontrado"}), 404
        
        cursor.execute(f"DELETE FROM Usuarios WHERE ID = {ID}")
        conexao.commit()
        
        return jsonify({"message" : "Usuario deletado com sucesso"}), 200
    except mysql.connector.Error as error:
        return jsonify({"error" : str(error)}), 500
    
    
    
    
    
