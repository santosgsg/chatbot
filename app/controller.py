import time

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
        while True:
            new = self.dvr.check_notification()

            if (new):
                numbers = self.dvr.get_numbers()
                if numbers:
                    if self.is_new(numbers):
                        print('Nova notificação')
                        Mysql_repository().save_new_numbers(numbers)  # salvar no banco
                        place = Mysql_repository().get_place()
                        message = Mysql_repository().get_mensagem('1').replace('#$%', place)

                        self.dvr.give_welcome(message)

                    else:
                        self.continue_chat()
            else:
                print('Nenhuma nova conversa identificada!')
                time.sleep(10)

    def is_new(self, numbers_list):

        pass
    #verificar na base se o numero tem historico

    def continue_chat(self):

        pass
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