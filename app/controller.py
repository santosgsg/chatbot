import time

from agendaapi.quickstart import createEvent
from app.web_driver import Driver
# from repository.banco import Repository
from banco import Mysql_repository


class Account:
    def __init__(self):
        self.dvr = None
        self.msg = ''

    def autenticar(self):
        self.dvr = Driver()
        image = self.dvr.search_img()
        return image

    def chat_loop(self):
        place = Mysql_repository().get_place()
        while True:
            new = self.dvr.check_notification()

            if (new):
                numbers = self.dvr.get_numbers()
                if numbers:
                    for number in numbers:
                        self.dvr.join_chat(number)
                        message_id = self.is_new(number)
                        back = 1
                        if not message_id:
                            print('Nova notificação')
                            Mysql_repository().save_new_number(number)  # salvar no banco
                            message = Mysql_repository().get_mensagem('1').replace('#$%', place)
                        else:
                            back = self.continue_chat(message_id, number)
                            if back:
                                message_id = Mysql_repository().check_new(number)
                                message = Mysql_repository().get_mensagem(message_id)
                                if message.find('#$%') != -1:
                                    message = message.replace('#$%', place)
                                if message.find('***') != -1:
                                    especialidades = Mysql_repository().get_especialidades()
                                    message = message.replace('***', especialidades)
                                if message.find('!!!') != -1:
                                    if back != 1:
                                        medicos = Mysql_repository().get_medico_by_especialidade(back)
                                        message = message.replace('***', medicos)
                        if back:
                            self.dvr.send_message(message)

                        self.dvr.click('_2WP9Q')
            else:

                print('Nenhuma nova conversa identificada!')
                time.sleep(10)

    def is_new(self, number):
        message_id = Mysql_repository().check_new(number)
        if message_id:
            print(f'Continuando chat com o numero {number}')
        else:
            print('Novo cliente')

        return message_id

    def continue_chat(self, message_id, number):
        c_message = self.dvr.get_last_message()

        if c_message == 'ag':
            createEvent('Sr Santana', '123456', 'Dr Excelentíssimo Santana', 'Uniceub',
                        '2019-12-01', '20:00:00', '2019-12-01', '21:00:00', 'teste@gmail.com', 'gabriel.sg@sempreceub.com')

#nomepaciente, codmedico, nomemedico, localizacao, datainicio, horainicio, datafim, horafim, emailpaciente, emailmedico

        if message_id[0] == '1':
            if len(message_id) == 1: #1
                if c_message == '1' or (c_message.upper().find('AGENDAR') != -1):
                    Mysql_repository().set_message_id('1-1', number)
                    return 1
                elif c_message == '2' or (c_message.upper().find('REMARCAR') != -1):
                    Mysql_repository().set_message_id('1-2', number)
                    self.remarcar_consulta()

                elif c_message == '3' or (c_message.upper().find('DESFAZER') != -1):
                    Mysql_repository().set_message_id('1-3', number)
                    self.desfazer_consulta()
                else:
                    self.not_recognized()
            elif len(message_id) == 3: #1-1 CPF
                if message_id[2] == '1':
                    cpf_result = self.verify_cpf(c_message.strip())
                    if cpf_result == 'not_int':
                        #Somente numeros
                        self.dvr.send_message('Por favor, digite somente números.\n')
                        return 0
                    if(cpf_result):
                        #CPF válido
                        c_message = c_message.strip()
                        nome = Mysql_repository().get_pessoa_nome(c_message)
                        if (nome):
                            Mysql_repository().set_message_id('1-1-1', number)
                            return 1
                        else:
                            contato_id = Mysql_repository().get_contato_id(number)
                            Mysql_repository().insert_pessoa_cpf(c_message, contato_id)
                            Mysql_repository().insert_paciente(c_message)

                            Mysql_repository().set_message_id('1-1-2', number)
                            return 1
                    else:
                        self.dvr.send_message('Cpf inválido.\nPor favor, digite um cpf válido.\n')
                        #CPF não é valido
                        return 0
            elif len(message_id) == 5:  # 1-1-1 ou 1-1-2
                if message_id[4] == '1':
                    if c_message == '1' or c_message.upper().find('BUSCAR'):
                        Mysql_repository().set_message_id('1-1-1-1', number)
                        return 1
                    if c_message == '2' or c_message.upper().find('ESCOLHER'):
                        Mysql_repository().set_message_id('1-1-1-2', number)
                        return 1
                elif message_id[4] == '2':
                    n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                    for c in c_message:
                        if c in n:
                            self.dvr.send_message('O Nome não pode conter dígitos.\n')
                            return 0

                    contato_id = Mysql_repository().get_contato_id(number)
                    Mysql_repository().set_pessoa_nome(nome=c_message, contato_id=contato_id)
                    Mysql_repository().set_message_id('1-1-2-1')
                    return 1

            elif len(message_id) == 7:  # 1-1-1-1
                if message_id[4] == '1' and message_id[6] == '1':
                    especialidade = None
                    especialidades = Mysql_repository().get_especialidades()
                    lista_e = especialidades.split('\n')
                    for e in lista_e:
                        if (e.upper().find(c_message.upper()) != -1) or (e[0] == c_message):
                            especialidade = e[:4]
                            break

                    if not especialidade:
                        self.dvr.send_message('Não entendi!\nCaso necessário, digite apenas o número ao lado da especialidade\n')
                        return 1
                    else:
                        Mysql_repository().set_message_id('1-1-1-1-1', number)
                        return especialidade

                elif message_id[4] == '1' and message_id[6] == '2':

                    Mysql_repository().set_message_id('1-1-1-2-1')

                elif message_id[4] == '2' and message_id[7] == '1':
                    if c_message == '1' or c_message.upper().find('BUSCAR'):
                        Mysql_repository().set_message_id('1-1-1-1', number)
                        return 1
                    if c_message == '2' or c_message.upper().find('ESCOLHER'):
                        Mysql_repository().set_message_id('1-1-1-2', number)
                        return 1






            # elif c_message == '4' or c_message.upper() == 'AGENDAR':
            #     Mysql_repository().set_message_id('1-1', number)



    def not_recognized(self):
        self.dvr.send_message('Não entendi, pode repetir?\n')

    def verify_cpf(self, cpf_str):
        try:
            cpf = int(cpf_str)

        except(Exception):
            return 'not_int'

        if len(cpf_str) == 11:
            return True
        else:
            return False

    def agendar_consulta(self):
        pass

    def remarcar_consulta(self):
        pass

    def desfazer_consulta(self):
        pass

    #verificar na base se o numero tem historico

        # obter historico na base


# class Academia:
#     def get_atividades(self):
#         return Mysql_repository().get_atividades()
#
#     def get_ficha(self):
#         return Mysql_repository().get_ficha()
#
#     def get_forma_pagamento(self):
#         return Mysql_repository().get_forma_pagamentos()
#
#     def get_equipamento(self):
#         return Mysql_repository().get_equipamentos()
#
#     def get_forma_pagamento_by_id(self, id):
#         return Mysql_repository().get_forma_pagamento_by_id(id)
#
#     def set_equipamentos(self, nome, obs):
#         Mysql_repository().set_equipamento(nome, obs)
#
#     def set_forma_pagamento(self, nome):
#         Mysql_repository().set_forma_pagamento(nome)
#
#     def update_forma_pagamento(self, id, nome):
#         Mysql_repository().update_forma_pagamento(id, nome)
#
#     def delete_forma_pagamento(self, id):
#         Mysql_repository().delete_forma_pagamento(id)
#
#     def delete_equipamento(self, id):
#         Mysql_repository().delete_equipamento(id)
    # def build_rows(self, content):
    #     result = ''
    #     for element in content:
    #         result += '''<tr class="row100">'''
    #         cont = 1
    #         for column in element:
    #             result += f'''
    #                     <td class="column100 column{cont}" data-column="column{cont}">{element[column]}</td>
    #                 '''
    #             cont += 1
    #         result += '</tr>\n'
    #     return result
    #
    # def build_columns(self, content):
    #     result = '''<tr class="row100">'''
    #     cont = 1
    #     for column in content[0]:
    #         result += f'''
    #                         <td class="column100 column{cont}" data-column="column{cont}">{column}</td>
    #                     '''
    #         cont += 1
    #     result += '</tr>\n'
    #     return result