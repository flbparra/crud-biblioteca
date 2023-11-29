CREATE DATABASE library_bixo;
USE library_bixo;

CREATE TABLE Livros (
    IDLivro INT NOT NULL PRIMARY KEY,
    Titulo VARCHAR(255) NOT NULL,
    Autor VARCHAR(255) NOT NULL,
    Descricao TEXT,
    Categoria VARCHAR(50),
    DataAquisicao DATE,
    EstadoConservacao VARCHAR(50),
    LocalizacaoFisica VARCHAR(100),
    URICapaLivro VARCHAR(255)
);

CREATE TABLE MateriaisDidaticos (
    IDMaterial INT NOT NULL PRIMARY KEY,
    Descricao TEXT,
    NumeroSerie VARCHAR(20),
    DataAquisicao DATE,
    EstadoConservacao VARCHAR(50),
    LocalizacaoFisica VARCHAR(100) NOT NULL,
    URIFotoMaterial VARCHAR(255)
);

CREATE TABLE Item (
    IDItem INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Tipo VARCHAR(20),
    IDLivro INT,
    IDMaterial INT,
    FOREIGN KEY (IDLivro) REFERENCES Livros(IDLivro),
    FOREIGN KEY (IDMaterial) REFERENCES MateriaisDidaticos(IDMaterial)
);

CREATE TABLE Usuarios (
    ID INT NOT NULL PRIMARY KEY,
    Nome VARCHAR(50),
    Sobrenome VARCHAR(50),
    Funcao VARCHAR(20),
    Login VARCHAR(50) UNIQUE,
    Senha VARCHAR(255),  
    URIFotoUsuario VARCHAR(255)
);

CREATE TABLE PermissaoUsuario (
    IDPermissao INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    UsuarioID INT,
    Permissao VARCHAR(50),
    FOREIGN KEY (UsuarioID) REFERENCES Usuarios(ID)
);

CREATE TABLE Emprestimos (
    IDUsuario INT,
    IDItem INT,
    DataEmprestimo DATE,
    DataDevolucaoPrevista DATE,
    StatusSituacao VARCHAR(20) CHECK (StatusSituacao IN ('ATRASADO', 'EM ANDAMENTO')),
    PRIMARY KEY (IDUsuario, IDItem),
    FOREIGN KEY (IDUsuario) REFERENCES Usuarios(ID),
    FOREIGN KEY (IDItem) REFERENCES Item(IDItem)
);

DELIMITER //
CREATE TRIGGER AtualizarDataDevolucaoPrevista
BEFORE INSERT ON Emprestimos
FOR EACH ROW
BEGIN
    IF NEW.DataDevolucaoPrevista < CURDATE() THEN
        SET NEW.StatusSituacao = 'ATRASADO';
    ELSE
        SET NEW.StatusSituacao = 'EM ANDAMENTO';
    END IF;
END;
//
DELIMITER ;
