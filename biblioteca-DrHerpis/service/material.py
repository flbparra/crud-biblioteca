from service.connectBD import getDB
from flask import jsonify, request


def create_new_material(IDMaterial, Descricao, NumeroSerie, Numero, DataAquisicao, EstadoConservacao, LocalizacaoFisicao, URICapaLivro):
    
    conexao = getDB()
    cursor = conexao.cursor()
    query = "INSERT INTO Material(IDMaterial, Descricao, NumeroSerie, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URIFotoMaterial) VALUES(%s, %s, %s, %s, %s, %s, %s)"
    
    cursor.execute(query, (IDMaterial, Descricao ,NumeroSerie, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URIFotoMaterial))
    conexao.commit()
    material_cadastrado = get_material_id(IDMaterial)
    conexao.close()
    return jsonify({"mensagem" : "Material cadastrado com suscesso!", "material": {material_cadastrado}})
    
def get_material_id(IDMaterial):
    conexao = getDB()
    cursor = conexao.cursor()
    
    cursor.execute(f"SELECT IDMaterial, Descricao ,NumeroSerie, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URIFotoMaterial FROM MaterialDidaticos WHERE IDMateria ={IDMaterial}")
    infoMaterial= []
    
    for row in cursor:
        IDMaterial, Descricao ,NumeroSerie, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URIFotoMaterial = row
        infoBook.append({
            "IDMaterial": IDMaterial,
            "Descricao": Descricao,
            "NumeroSerie": NumeroSerie,
            "DataAquisicao": DataAquisicao,
            "EstadoConservacao": EstadoConservacao,
            "LocalizacaoFisica": LocalizacaoFisica,
            "URIFotoMaterial": URIFotoMaterial
        })
           
    conexao.close()
    return jsonify(infoMaterial)

def get_all_materials():
    pass

def delete_material(IDMaterial):
    pass

def update_material(IDMaterial):
    pass