from flask import Flask, request

from service.livros import create_new_book, get_book_id, get_all_books, delete_book, update_book, get_books_category, get_books_titles, get_books_author

from service.material import create_new_material, get_material_id, get_all_materials, delete_material, update_material

from service.usuario import create_new_user, get_user_id, get_all_users, delete_user, update_user
from service.login import render_login

import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# /HOME criado
@app.route('/')
def index():
    return "HELLO AMIGO!"

@app.route('/login', methods=['POST'])
def login_this_user():
    login_data = request.json
    return render_login(login_data)

@app.route('/books', methods=['GET'])
def view_books():
# ---> Retorna todos os livros cadastrados no banco de dados
    return get_all_books()


@app.route("/books/<int:IDLivro>", methods=["GET"])
# ---> Função para visualizar livro por id
def view_book_id(IDLivro):
    return get_book_id(IDLivro)

@app.route("/books/<string:titulo>", methods=["GET"])
# ---> Função para visualizar livros por titulo
def view_books_title(titulo):
    return get_books_titles(titulo)

@app.route("/books/authors/<string:author>", methods=["GET"])
# ---> Função para visualizar livros por autores
def view_books_author(author):
    return get_books_author(author)

@app.route("/books/<string:categoria>", methods=["GET"])
# ---> Retorna todos que tem as categorias cadastrados no banco de dados
def view_books_category(categoria):
    return get_book_category(categoria)
    

@app.route("/books/<int:IDLivro>", methods=["POST"])
# ---> Função para criar livro
def create_book(IDLivro):
    livro_data = request.json
    return create_new_book(
        IDLivro, 
        livro_data['Titulo'], 
        livro_data['Autor'], 
        livro_data['Descricao'], 
        livro_data['Categoria'], 
        livro_data['DataAquisicao'], 
        livro_data['EstadoConservacao'],
        livro_data['LocalizacaoFisica'],
        livro_data['URICapaLivro'] 
        )

@app.route("/books/<int:IDLivro>", methods=["DELETE"])
# ---> Função para deletar livro
def delete_this_book(IDLivro):
    return delete_book(IDLivro)

@app.route("/books/<int:IDLivro>", methods=["PUT"])
# ---> Função para atualizar livro
def update_this_book(IDLivro):
    return update_book(IDLivro)



"""
MATERIAS - INSERT, CONSULTA, DELETE, UPDATE
"""

@app.route('/materials/<int:IDMaterial>', methods=['POST'])
def create_material(IDMaterial):
    material_data = request.json
    return create_new_material(
        IDMaterial, 
        material_data['Descricao'],material_data['NumeroSerie'], material_data['DataAquisicao'],material_data['EstadoConservacao'],
        material_data['LocalizacaoFisica'],
        material_data['URIFotoMaterial'])

@app.route('/materials/<int:IDMaterial>', methods=['GET']) 
def get_material(IDMaterial):
    return get_material_id(IDMaterial)

@app.route('/materials', methods=['GET'])
def view_materials():
    return get_all_materials()

@app.route('/materials/<int:IDMaterial>', methods=['GET'])
def view_material_id(IDMaterial):
    return get_material_id(IDMaterial)
    
@app.route('/materials/<int:IDMaterial>', methods=['DELETE'])
#somente admins podem deletar dados do banco
def delete_this_material(IDMaterial):
    return delete_material(IDMaterial)

@app.route('/materials/<int:IDMaterial>', methods=['PUT'])
# ---> Atualiza material, somente admin e chefes tem acessos
def upadate_this_material(IDMaterial):
    material_data = request.json
    return update_material(IDMaterial, material_data)



"""
USUARIOS: Chamadas para usuarios.
"""

@app.route('/user/<int:ID>', methods=['POST'])
# ---> Create new user
def create_user(ID):
    user_data = request.json
    return create_new_user(ID,
                       user_data['Nome'], 
                       user_data['Sobrenome'], 
                       user_data['Funcao'],
                       user_data['Login'], 
                       user_data['Senha'], 
                       user_data['URIFotoUsuario']
                       )
@app.route('/user/<int:ID>', methods=['GET'])
# Retorna usuarios por ID
def view_this_user(ID):
    return get_user_id(ID)
@app.route('/users', methods=['GET'])
# --> Retorna todos os usuarios
def view_all_users():
    return get_all_users()
@app.route('/user/<int:ID>', methods=['DELETE'])
# --> Delete a user por ID
def delete_this_user(ID):
    return delete_user(ID)
@app.route('/user/<int:ID>', methods=['PUT'])
# --> Update a user por ID (não a senha e nem o login)
def upadate_this_user(ID):
    return update_user(ID)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1', debug=True)

