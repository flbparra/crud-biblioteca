-- Script para popular Livros

INSERT INTO Livros(IDLivro, Titulo, Autor, Descricao, Categoria, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URICapaLivro) VALUES(2093871637, "Alice nos País das Maravilhas", "DISNEY", "Alice se aventurando.", "Fantasia", "2023-11-27", "Bom", "Estante 2", "URL_capa_livro");

INSERT INTO Livros(IDLivro, Titulo, Autor, Descricao, Categoria, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URICapaLivro) VALUES(1395026783, "Romeu e Julieta", "Sheakspeare", "Um romance de época.", "Romance", "2023-11-27", "Regular", "Estante 5", "URL_capa_livro");

INSERT INTO Livros(IDLivro, Titulo, Autor, Descricao, Categoria, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URICapaLivro) VALUES(1927384901, "Dom Casmurro", "Machado de Assis", "Drama e suspense entre Capitu e Bentinho.", "Drama", "2023-11-27", "Bom", "Estante 1", "URL_capa_livro");

INSERT INTO Livros(IDLivro, Titulo, Autor, Descricao, Categoria, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URICapaLivro) VALUES(1728390461, "Bíblia", "James King", "Bíblia sagrada.", "Religião", "2023-11-27", "Bom", "Estante 2", "URL_capa_livro");

INSERT INTO Livros(IDLivro, Titulo, Autor, Descricao, Categoria, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URICapaLivro) VALUES(1374871027, "Surely Youre Joking , MR. Feynman!", "Richard P. Feynman", "Aventuras de um personagem curioso.", "Biografia", "2023-11-27", "Ruim", "Estante 7", "URL_capa_livro");

-- Script para popular Materiais

INSERT INTO MateriaisDidaticos(IDMaterial, Descricao, NumeroSerie, Categoria, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URIFotoMaterial) VALUES(113, "Caneta Preta", "10851", "Material de Mesa", "2023-11-28", "Novo", "Estante 12", "URL_foto_caneta"); 

INSERT INTO MateriaisDidaticos(IDMaterial, Descricao, NumeroSerie, Categoria, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URIFotoMaterial) VALUES(114, "Tesoura", "12443", "Material de Mesa", "2023-11-28", "Bom", "Estante 12", "URL_foto_tesoura");

INSERT INTO MateriaisDidaticos(IDMaterial, Descricao, NumeroSerie, Categoria, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URIFotoMaterial) VALUES(115, "Notebook Samsung", "36858", "Eletrônico", "2022-06-12", "Bom", "Estante 17", "URL_foto_notebook");

INSERT INTO MateriaisDidaticos(IDMaterial, Descricao, NumeroSerie, Categoria, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URIFotoMaterial) VALUES(116, "Tablet Lenovo", "14586", "Eletrônico", "2022-06-12", "Regular", "Estante 18", "URL_foto_tablet");

INSERT INTO MateriaisDidaticos(IDMaterial, Descricao, NumeroSerie, Categoria, DataAquisicao, EstadoConservacao, LocalizacaoFisica, URIFotoMaterial) VALUES(117, "Perfurador de Papel", "17564", "Material de Mesa", "2023-11-28", "Bom", "Estante 12", "URL_foto_perfurador");

-- Script para popular Usuarios

INSERT INTO Usuarios(ID, Nome, Sobrenome, Funcao, Login, Senha, URIFotoUsuario) VALUES(324, "Henrique", "Oliveira", "Admin", "hos1r1s", "senha123", "URL_foto_usuario");

INSERT INTO Usuarios(ID, Nome, Sobrenome, Funcao, Login, Senha, URIFotoUsuario) VALUES(325, "Fabio", "Parra", "Chefe", "FLParra", "senha456", "URL_foto_usuario");

INSERT INTO Usuarios(ID, Nome, Sobrenome, Funcao, Login, Senha, URIFotoUsuario) VALUES(326, "Daniel", "Guimaraes", "Usuario", "Dmelo", "senha789", "URL_foto_usuario");

INSERT INTO Usuarios(ID, Nome, Sobrenome, Funcao, Login, Senha, URIFotoUsuario) VALUES(327, "Pedro", "Henrique", "Usuario", "PH", "senha110", "URL_foto_usuario");

INSERT INTO Usuarios(ID, Nome, Sobrenome, Funcao, Login, Senha, URIFotoUsuario) VALUES(328, "Silvio", "Silva", "Usuario", "Silvio", "senha112", "URL_foto_usuario");

-- Script para popular Itens

INSERT INTO Item(Tipo, IDLivro, IDMaterial, StatusItem) VALUES("Livro", 2093871637, Null, "Disponivel");

INSERT INTO Item(Tipo, IDLivro, IDMaterial, StatusItem) VALUES("Material", Null, 113, "Disponivel");

INSERT INTO Item(Tipo, IDLivro, IDMaterial, StatusItem) VALUES("Livro", 1395026783, Null, "Disponivel");

INSERT INTO Item(Tipo, IDLivro, IDMaterial, StatusItem) VALUES("Material", Null, 114, "Disponivel");

INSERT INTO Item(Tipo, IDLivro, IDMaterial, StatusItem) VALUES("Livro", 1927384901, Null, "Disponivel");

INSERT INTO Item(Tipo, IDLivro, IDMaterial, StatusItem) VALUES("Material", Null, 115, "Disponivel");

INSERT INTO Item(Tipo, IDLivro, IDMaterial, StatusItem) VALUES("Livro", 1728390461, Null, "Disponivel");

INSERT INTO Item(Tipo, IDLivro, IDMaterial, StatusItem) VALUES("Material", Null, 116, "Disponivel");

INSERT INTO Item(Tipo, IDLivro, IDMaterial, StatusItem) VALUES("Livro", 1374871027, Null, "Disponivel");

INSERT INTO Item(Tipo, IDLivro, IDMaterial, StatusItem) VALUES("Material", Null, 117, "Disponivel");