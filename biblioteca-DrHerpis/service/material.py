from service.connectBD import getDB
from flask import jsonify, request
import mysql.connector


def create_new_material(IDMaterial, Descricao, NumeroSerie, Categoria, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URIFotoMaterial):
    
    conexao = getDB()
    cursor = conexao.cursor()
    query = "INSERT INTO MateriaisDidaticos(IDMaterial, Descricao, NumeroSerie, Categoria, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URIFotoMaterial) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    
    cursor.execute(query, (IDMaterial, Descricao ,NumeroSerie, Categoria, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URIFotoMaterial))
    conexao.commit()
    material_cadastrado = get_material_id(IDMaterial)
    material_cadastrado = material_cadastrado.get_json()
    
    #----------------------------------------------------------------------------------------
    # Script para adicionar Material também na tabela Item
    adicionarEmItem = "INSERT INTO Item(Tipo, IDMaterial, StatusItem) VALUES (%s, %s, %s)"
    cursor.execute(adicionarEmItem,("Material", IDMaterial, "Disponivel"))
    conexao.commit()
    conexao.close()
    
    return jsonify({"mensage" : "Material cadastrado com sucesso", "material" :material_cadastrado}), 200
    
def get_material_id(IDMaterial):
    conexao = getDB()
    cursor = conexao.cursor()
    
    cursor.execute(f"SELECT IDMaterial, Descricao ,NumeroSerie, Categoria, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URIFotoMaterial FROM MateriaisDidaticos WHERE IDMaterial ={IDMaterial}")
    infoMaterial= []
    
    for row in cursor:
        IDMaterial, Descricao ,NumeroSerie, Categoria, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URIFotoMaterial = row
        infoMaterial.append({
            "IDMaterial": IDMaterial,
            "Descricao": Descricao,
            "NumeroSerie": NumeroSerie,
            "Categoria": Categoria,
            "DataAquisicao": DataAquisicao,
            "EstadoConservacao": EstadoConservacao,
            "LocalizacaoFisica": LocalizacaoFisica,
            "URIFotoMaterial": URIFotoMaterial
        })
           
    conexao.close()
    return jsonify(infoMaterial)

def get_all_materials():
    conexao = getDB()
    cursor  = conexao.cursor()
    
    cursor.execute("SELECT IDMaterial,Descricao, NumeroSerie, Categoria, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URIFotoMaterial FROM MateriaisDidaticos")
    
    allMateriais=[]
    
    for row in cursor:
        IDMaterial,Descricao, NumeroSerie, Categoria, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URIFotoMaterial = row
        
        allMateriais.append(
            {
            "IDMaterial": IDMaterial,
            "Descricao": Descricao,
            "NumeroSerie": NumeroSerie,
            "Categoria": Categoria,
            "DataAquisicao": DataAquisicao,
            "EstadoConservacao": EstadoConservacao,
            "LocalizacaoFisica": LocalizacaoFisica,
            "URIFotoMaterial": URIFotoMaterial
            })
    conexao.close()
    return jsonify({
        "Material cadastrado no sistema": allMateriais
    })
        
def delete_material(IDMaterial):
    
    conexao = getDB()
    cursor = conexao.cursor()
    
    try:
        #verifica se o id existe no banco
        
        cursor.execute(f"SELECT IDMaterial FROM MateriaisDidaticos WHERE IDMaterial = {IDMaterial}")
        Material_exite = cursor.fetchone()
        
        if not Material_exite:
            return jsonify({"message" : "Material não encontrado"}), 404
        
        cursor.execute(f"DELETE FROM Item WHERE IDLivro = {IDMaterial}")
        cursor.execute(f"DELETE FROM MateriaisDidaticos WHERE IDMaterial = {IDMaterial}")
        conexao.commit()
        
        return jsonify({"message" : "Material deletado com sucesso!"}), 200
    
    except mysql.connector.Error as erro:
        return jsonify({"error" : str(erro)}), 500
    

def update_material(IDMaterial):
    conexao = getDB()
    cursor = conexao.cursor()
    
    cursor.execute(f"SELECT IDMaterial FROM MateriaisDidaticos WHERE IDMaterial = {IDMaterial}")
    material_exite = cursor.fetchone()
        
    if not material_exite:
        conexao.close()
        return jsonify({"message" : "Material não encontrado"}), 404
    
    material_data = request.json

    query = "UPDATE MateriaisDidaticos SET Descricao=%s, NumeroSerie=%s, Categoria=%s, DataAquisicao=%s, EstadoConservacao=%s, LocalizacaoFisica=%s, URIFotoMaterial=%s WHERE IDMaterial=%s"
        
    cursor.execute(query,(material_data.get('Descricao'),
            material_data.get('NumeroSerie'),
            material_data.get('Categoria'),
            material_data.get('DataAquisicao'),
            material_data.get('EstadoConservacao'),
            material_data.get('LocalizacaoFisica'),
            material_data.get('URIFotoMaterial'),
            IDMaterial))
        
    conexao.commit()
    conexao.close()
    return jsonify({"message" : "Material atualizado"})
        
        
    
    
