from service.connectBD import getDB
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


def cripto_senha():
    #fazer função para criptografia senha.
    pass

def create_user(ID, Nome, Sobrenome, Login, Senha, URIFotoUsuario):
    
    conexao = getDB()
    cursor = conexao.cursor()
    senha_crypt = bcrypt.generate_password_hash(Senha).decode('utf-8')
    
    query = "INSERT INTO Usuarios(ID, Nome, Sobrenome, Login, Senha, URIFotoUsuario) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    
    
    cursor.execute(query, (ID, Nome, Sobrenome, Login, senha_crypt, URIFotoUsuario))
    conexao.commit()
    
    usuario_cadastrado = get_user_id(ID)
    usuario_cadastrado = usuario_cadastrado.get_json()
    
    conexao.close()
    
    return jsonify({"mensage" : "Usuario cadastrado com sucesso", "Usuario" : usuario_cadastrado }), 200


def get_user_id(ID):
    
    conexao = getDB()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT ID, Nome, Sobrenome, Funcao, URIFotoUsuario FROM Usuario WHERE ID = {ID}")
    
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


def get_all_user():
    
    conexao = getDB()
    cursor = conexao.cursor()

    cursor.execute("SELECT ID, Nome, Sobrenome, Funcao, URIFotoUsuario FROM Usuarios")
    
    allUser = []
    
    for rom in cursor:
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
    
def update_user():
    pass

def delete_user():
    pass
    
    
    
