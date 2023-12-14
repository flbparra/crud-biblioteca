from service.connectBD import getDB
from flask import jsonify

def create_new_emprestimo(data):
    
    IDUsuario = data.get('IDUsuario')
    IDItem = data.get('IDItem')

    conexao = getDB()
    cursor = conexao.cursor()

    status = "SELECT StatusItem FROM Item WHERE IDItem = {0}".format(IDItem)
    cursor.execute(status)
    status_item = cursor.fetchone()

    if status_item[0] == "Disponivel":
        
        consulta_data = "SELECT CURDATE()"
        cursor.execute(consulta_data)
        data_emprestimo = cursor.fetchall()

        nova_data = "SELECT ADDDATE('{0}', INTERVAL 31 DAY)".format(data_emprestimo[0][0])
        cursor.execute(nova_data)
        data_limite = cursor.fetchall()
        
        query = "INSERT INTO Emprestimos(IDUsuario, IDItem, DataEmprestimo, DataDevolucaoPrevista) VALUES(%s, %s, %s, %s)"
        cursor.execute(query, (IDUsuario, IDItem, data_emprestimo[0][0], data_limite[0][0]))

        mudar_status = "UPDATE Item SET StatusItem = 'Indisponivel' WHERE IDItem = {0}".format(IDItem)
        cursor.execute(mudar_status)

        conexao.commit()
        conexao.close()

        return jsonify({"message" : "Emprestimo realizado com sucesso"})
    
    else:
        return jsonify({"message" : "Esse livro esta indisponivel"})
    



def get_emprestimo(IDUsuario):

    conexao = getDB()
    cursor = conexao.cursor()

    retornar = "SELECT * FROM Emprestimos WHERE IDUsuario = {0}".format(IDUsuario)
    cursor.execute(retornar)
    
    emprestimos = []

    for row in cursor:
        
        IDUser, IDItem, DataEmprestimo, DataDevolucaoPrevista, StatusSituacao = row

        emprestimos.append(
            {
                "IDUsuario": IDUser,
                "IDItem": IDItem,
                "Data do Emprestimo": DataEmprestimo,
                "Data de devolução": DataDevolucaoPrevista,
                "Situação do Item": StatusSituacao
            }
        ) 

    conexao.close()

    return jsonify({"Emprestimos do usuário" : emprestimos})




def delete_emprestimo(IDItem):

    conexao = getDB()
    cursor = conexao.cursor()

    consulta_data_inicial = "SELECT DataEmprestimo FROM Emprestimos WHERE IDItem = {0}".format(IDItem)
    cursor.execute(consulta_data_inicial)
    data_inicial = cursor.fetchone()

    consulta_data_limite = "SELECT DataDevolucaoPrevista FROM Emprestimos WHERE IDItem = {0}".format(IDItem)
    cursor.execute(consulta_data_limite)
    data_limite = cursor.fetchone()

    consulta_diferenca = "SELECT DATEDIFF('{0}','{1}')".format(data_limite[0], data_inicial[0])
    cursor.execute(consulta_diferenca)
    diferenca = cursor.fetchone()
    diferenca = int(diferenca[0])

    if diferenca >= 0:
        exclude = "DELETE FROM Emprestimos WHERE IDItem = {0}".format(IDItem)
        cursor.execute(exclude)

        mudar_status = "UPDATE Item SET StatusItem = 'Disponivel' WHERE IDItem = {0}".format(IDItem)
        cursor.execute(mudar_status)

        conexao.commit()
        conexao.close()

        return jsonify({"message" : "Item devolvido com sucesso"})
    
    else:
        return jsonify({"message" : "Seu emprestimo está atrasado em {0} dias, para prosseguir vá até a BCE e pague a taxa.".format(diferenca)})
    


def update_emprestimo(IDItem):

    conexao = getDB()
    cursor = conexao.cursor()

    consulta_data_inicial = "SELECT DataEmprestimo FROM Emprestimos WHERE IDItem = {0}".format(IDItem)
    cursor.execute(consulta_data_inicial)
    data_inicial = cursor.fetchone()

    consulta_data_limite = "SELECT DataDevolucaoPrevista FROM Emprestimos WHERE IDItem = {0}".format(IDItem)
    cursor.execute(consulta_data_limite)
    data_limite = cursor.fetchone()

    consulta_diferenca = "SELECT DATEDIFF('{0}','{1}')".format(data_limite[0], data_inicial[0])
    cursor.execute(consulta_diferenca)
    diferenca = cursor.fetchone()
    diferenca = int(diferenca[0])

    if diferenca >= 0:

        nova_data = "SELECT ADDDATE(CURDATE(), INTERVAL 31 DAY)"
        cursor.execute(nova_data)
        data_limite = cursor.fetchone()

        att_emprestimo = "UPDATE Emprestimos SET DataDevolucaoPrevista = '{0}' WHERE IDItem = {1}".format(data_limite[0], IDItem)
        cursor.execute(att_emprestimo)

        conexao.commit()
        conexao.close()

        return jsonify({"message" : "Emprestimo renovado com sucesso"})

    else:

        return jsonify({"message" : "Seu emprestimo está atrasado, primeiro pague a taxa na BCE."})