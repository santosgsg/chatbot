import time

from app.web_driver import Driver
from repository.database import Repository


class Account:
    def __init__(self):
        self.dvr = None
        self.msg = ''

    def autenticar(self):
        self.dvr = Driver()
        image = self.dvr.search_img()
        return image

    def identify_new_message(self):

        while True:
            new = self.dvr.check_notification()

            if (new):
                numbers = self.dvr.get_numbers()
                if numbers:
                    if self.is_new(numbers):
                        Repository().save_new_numbers(numbers)  # salvar no banco
                        print('Nova notificação')
                        self.dvr.give_welcome()

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