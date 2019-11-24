import mysql.connector


class Mysql_repository:

    def __init__(self):
        self.con = mysql.connector.connect(host="34.95.202.115", user="root", passwd="123456")

    def save_new_number(self, number):
        cursor = self.con.cursor()
        cursor.execute(f'INSERT INTO bot.Contato (numero, idMensagem) VALUES ("{number}")')
        self.con.commit()
        cursor.close()
        self.con.close()
        pass

    def get_mensagem(self, id):
        cursor = self.con.cursor()
        cursor.execute(f'SELECT descricao FROM bot.Mensagem where idMensagem = {id}')
        result = ''
        for descricao in cursor:
            result = descricao[0]
        cursor.close()
        self.con.close()
        return result
        pass

    def get_place(self):
        cursor = self.con.cursor()
        cursor.execute(f'SELECT * FROM bot.CLINICA where id = 1')
        for NOME_CLINICA in cursor:
            result = NOME_CLINICA[0]
        cursor.close()
        self.con.close()
        return result
    # def get_atividades(self):
    #     cursor = self.con.cursor()
    #     cursor.execute("SELECT * FROM mydb.Atividades")
    #     result = {'header': ['Nome', 'Especialidade', 'Dia', 'HrInicio', 'HrFim'], 'body': []}
    #     for (Nome, Sexo, Especialidade, Dia, HrInicio, HrFim) in cursor:
    #         result['body'].append({'Nome': Nome
    #                                , 'Especialidade': Especialidade
    #                                , 'Dia': Dia
    #                                , 'HrInicio': HrInicio
    #                                , 'HrFim': HrFim})
    #     cursor.close()
    #     self.con.close()
    #     return result
    #
    # def get_ficha(self):
    #     cursor = self.con.cursor()
    #     cursor.execute("SELECT * FROM mydb.ficha")
    #     result = {'header': ['Aluno', 'DtInicio', 'DtFim', 'Equipamento', 'Carga', 'Serie', 'Repetição'], 'body': []}
    #     for (Aluno, DtInicio, DtFim, Equipamento, carga, serie, repeticao) in cursor:
    #         result['body'].append({'Aluno': Aluno
    #                               , 'DtInicio': DtInicio
    #                               , 'DtFim': DtFim
    #                               , 'Equipamento': Equipamento
    #                               , 'Carga': carga
    #                               , 'Serie': serie
    #                               , 'Repetição': repeticao})
    #     cursor.close()
    #     self.con.close()
    #     return result
    #
    # def get_forma_pagamentos(self):
    #     cursor = self.con.cursor()
    #     cursor.execute("SELECT * FROM mydb.TbFormaPagamento")
    #     result = {'method_delete': 'delete_forma_pagamento', 'method': 'cadastro_forma_pagamento', 'header': ['Id', 'Nome'], 'body': []}
    #     for (PkFormaPagamento, Nome) in cursor:
    #         result['body'].append({'Id': str(PkFormaPagamento)
    #                               , 'Nome': Nome})
    #     cursor.close()
    #     self.con.close()
    #     return result
    #
    # def update_forma_pagamento(self, id, nome):
    #     cursor = self.con.cursor()
    #     cursor.execute(f"UPDATE mydb.TbFormaPagamento SET Nome = '{nome}' WHERE PkFormaPagamento = '{id}'")
    #     self.con.commit()
    #     cursor.close()
    #     self.con.close()
    #
    # def get_equipamentos(self):
    #     cursor = self.con.cursor()
    #     cursor.execute("SELECT * FROM mydb.TbEquipamento")
    #     result = {'method_delete': 'delete_equipamento', 'method': 'cadastro_equipamento', 'header': ['Id', 'Nome', 'Observação'], 'body': []}
    #     for (Pk_equipamento, Nome, Observacao) in cursor:
    #         result['body'].append({'Id': str(Pk_equipamento)
    #                               , 'Nome': Nome
    #                               , 'Observacao': Observacao})
    #     cursor.close()
    #     self.con.close()
    #     return result
    #
    # def get_forma_pagamento_by_id(self, id):
    #     cursor = self.con.cursor()
    #     cursor.execute(f"SELECT * FROM mydb.TbFormaPagamento WHERE PkFormaPagamento = {id}")
    #     for (PkFormaPagamento, Nome) in cursor:
    #         result = {'Id': PkFormaPagamento, 'Nome': Nome}
    #
    #     cursor.close()
    #     self.con.close()
    #     return result
    #     # cursor.execute(f"UPDATE mydb.TbFormaPagamento SET Nome = '{}' WHERE address = '{}'")
    #
    # def set_equipamento(self, nome, obs):
    #     cursor = self.con.cursor()
    #     cursor.execute(f'INSERT INTO mydb.TbEquipamento (Nome, Observacao) VALUES ("{nome}", "{obs}")')
    #     self.con.commit()
    #     cursor.close()
    #     self.con.close()
    #
    # def set_forma_pagamento(self, nome):
    #     cursor = self.con.cursor()
    #     cursor.execute(f'INSERT INTO mydb.TbFormaPagamento (Nome) VALUES ("{nome}")')
    #     self.con.commit()
    #     cursor.close()
    #     self.con.close()
    #
    # def delete_forma_pagamento(self, id):
    #     cursor = self.con.cursor()
    #     cursor.execute(f'DELETE FROM mydb.TbFormaPagamento where PkFormaPagamento = {id}')
    #     self.con.commit()
    #     cursor.close()
    #     self.con.close()
    #
    # def delete_equipamento(self, id):
    #     cursor = self.con.cursor()
    #     cursor.execute(f'DELETE FROM mydb.TbEquipamento where Pk_equipamento = {id}')
    #     self.con.commit()
    #     cursor.close()
    #     self.con.close()
    # # def set_equipamento(self, nome, obs):
