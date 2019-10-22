import time

from app.web_driver import driver

class Account:
    def __init__(self):
        self.dvr = None
        self.msg = ''

    def autenticar(self):
        self.dvr = driver()
        image = self.dvr.search_img()
        return image

    def identify_new_message(self):

        while True:
            new = self.dvr.check_notification()

            if (new):
                print('Nova notificação')
                self.dvr.give_welcome()
            else:
                print('Nenhuma nova conversa identificada!')
                time.sleep(10)
