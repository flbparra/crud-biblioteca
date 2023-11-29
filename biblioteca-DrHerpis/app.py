from flask import Flask, request
from service.livros import create_new_book, get_book_id, get_all_books, delete_book, update_book
from service.material import create_new_material, get_material_id, get_all_materials, delete_material, update_material


app = Flask(__name__)


# /HOME criado
@app.route('/')
def index():
    return "HELLO AMIGO!"


@app.route('/books', methods=['GET'])
def view_books():
    return get_all_books()


@app.route("/books/<int:IDLivro>", methods=["GET"])
# ---> Função para visualizar livro por id
def view_book_id(IDLivro):
    return get_book_id(IDLivro)


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
def delete_this_material(IDMaterial):
    return delete_material(IDMaterial)

def upadate_this_material(IDMaterial):
    return update_material(IDMaterial)

if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1', debug=True)

