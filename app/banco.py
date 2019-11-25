import mysql.connector


class Mysql_repository:

    def __init__(self):
        self.con = mysql.connector.connect(host="34.95.202.115", user="root", passwd="123456")

    def finalize(self, cursor):
        cursor.close()
        self.con.close()

    def save_new_number(self, number):
        cursor = self.con.cursor()
        cursor.execute(f'INSERT INTO bot.Contato (numero, idMensagem) VALUES ("{number}", "1")')
        self.con.commit()
        self.finalize(cursor)

    def get_mensagem(self, id):
        cursor = self.con.cursor()
        cursor.execute(f"SELECT descricao FROM bot.Mensagem where idMensagem = '{id}'")
        result = ''
        for descricao in cursor:
            result = descricao[0]
        self.finalize(cursor)
        return result

    def get_place(self):
        cursor = self.con.cursor()
        cursor.execute(f'SELECT NOME_CLINICA FROM bot.CLINICA where PK_CNPJ = 83539602000149')
        for nome in cursor:
            result = nome[0]
        self.finalize(cursor)
        return result

    def check_new(self, number):
        cursor = self.con.cursor()
        result = None
        cursor.execute(f'SELECT idMensagem FROM bot.Contato where numero = "{number}"')
        for idMensagem in cursor:
            result = idMensagem[0]
        self.finalize(cursor)

        return result

    def set_message_id(self, message_id, number):
        cursor = self.con.cursor()
        cursor.execute(f"UPDATE bot.Contato SET idMensagem = '{message_id}' WHERE numero = '{number}'")
        self.con.commit()
        self.finalize(cursor)

    def get_pessoa_nome(self, cpf):
        cursor = self.con.cursor()
        result = None
        #SELECT PK_CPF, NOME, fk_contato, fk_endereco, fk_plano_saude, numero_plano FROM bot.PESSOA;
        cursor.execute(f'SELECT NOME FROM bot.PESSOA where PK_CPF = "{cpf}"')
        for nome in cursor:
            result = nome[0]
        self.finalize(cursor)
        return result

    def insert_pessoa_cpf(self, cpf, idContato):
        cursor = self.con.cursor()
        cursor.execute(f"INSERT INTO bot.PESSOA(PK_CPF, fk_contato)VALUES('{cpf}', '{idContato}');")
        self.con.commit()
        self.finalize(cursor)

    def get_contato_id(self, number):
        cursor = self.con.cursor()
        result = None
        # SELECT PK_CPF, NOME, fk_contato, fk_endereco, fk_plano_saude, numero_plano FROM bot.PESSOA;
        cursor.execute(f'SELECT idContato FROM bot.Contato where numero = "{number}"')
        for contato_id in cursor:
            result = contato_id[0]
        self.finalize(cursor)
        return result

    def set_pessoa_nome(self, nome, contato_id):
        cursor = self.con.cursor()
        cursor.execute(f"UPDATE bot.PESSOA SET NOME = '{nome}' WHERE fk_contato = '{contato_id}'")
        self.con.commit()
        self.finalize(cursor)

    def get_especialidades(self):
        cursor = self.con.cursor()
        result = ' '
        cursor.execute(f'select distinct especialidade from bot.MEDICO;')
        cont = 1
        for especialidade in cursor:
            result += +especialidade[0]+'\n'
            cont += 1

        self.finalize(cursor)
        return result

    def get_medico_by_especialidade(self, especialidade):
        cursor = self.con.cursor()
        result = None
        cursor.execute(f'SELECT p.NOME FROM bot.MEDICO m, bot.PESSOA p WHERE p.PK_CPF = m.PESSOA_PK_CPF and m.ESPECIALIDADE like %{especialidade}%;')
        cont = 1
        for nome in cursor:
            result += f'{nome[0]}\n'
            cont += 1
        self.finalize(cursor)
        return result

    def get_medico_by_nome(self, nome):
        cursor = self.con.cursor()
        result = None
        cursor.execute(
            f'SELECT c.DATA_CONSULTA, c.HORA_INICIO FROM bot.MEDICO m, bot.PESSOA p, bot.CONSULTA c, bot.PACIENTE pc '
            f'WHERE p.PK_CPF = m.PESSOA_PK_CPF and pc.PESSOA_PK_CPF = p.PK_CPF and c.PACIENTE_PK_Id = pc.PK_Id '
            f'and p.NOME like %{nome}%;')
        cont = 1
        for (dt_consulta, hr_inicio) in cursor:
            result += f'{cont}: {dt_consulta} - {hr_inicio[0]}\n'
            cont += 1
        self.finalize(cursor)
        return result

    def insert_paciente(self, cpf):
        cursor = self.con.cursor()
        cursor.execute(f"INSERT INTO bot.PACIENTE(PESSOA_PK_CPF)VALUES('{cpf}');")
        self.con.commit()
        self.finalize(cursor)

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
