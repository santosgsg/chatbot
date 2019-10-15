from app.web_driver import driver

class Account:
    def __init__(self):
        self.msg = ''

    def autenticar(self):
        image = driver().search_img()
        return image