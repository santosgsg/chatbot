class Mensagem:

    @staticmethod

    def welcome(place='Não identificado'):
        return f'Olá, esse é o serviço de agendamento de consultas do estabelecimento {place}. O que você deseja fazer?\nAGENDAR CONSULTA\nREMARCAR CONSULTA\nDESFAZER CONSULTA\n'
