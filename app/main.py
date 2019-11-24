import threading

from flask import Flask, render_template, url_for
from flask import request
import json

from werkzeug.utils import redirect

from app.controller import Account  # , Academia
from templates import Template

app = Flask(__name__)

@app.route('/chatbot')
def index():
    acc = Account()
    img = acc.autenticar()
    t = threading.Thread(name='Check', target=acc.chat_loop)
    t.start()
    print('Thread iniciada')

    return "<div style='display: block; text-align: center;'>" \
           "<strong> Bem vindo ao chatbot <br> Primeiro autentique seu whatsapp no qrcode abaixo: </strong><br> <br> " \
           f'<img alt="Scan me!" src="{img}" >' \
           "<br> <br> Iremos conectar nossa aplicação com sua conta do whatsapp para poder enviar e receber mensagens. <br>" \
           "<strong>OBS:</strong> Caso ocorra algum erro de leitura, atualize a pagina (f5) <br>" \
           "Metodos registrados: <br>" \
           "/enviar" \
           "</div>"

@app.route('/nome/<name>&<sn>')
def calculate_param(name, sn):
    return f'Bem vindo {name} {sn}'

@app.route('/teste')
def teste():
    data = '<img alt="Scan me!" src="data:image/png;base64,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" >'
    return data

# @app.route('/autenticar')
# def autenticate():
#     qr_code = Account.autenticar()
#     return qr_code

@app.route('/enviar', methods=['POST'])
def post():
    data = request.form
    print(json.dumps(data))
    return {'Response': 'sucesso'}

# @app.route('/listar-atividades')
# def getAtividades():
#     lista_atividades = Academia().get_atividades()
#     return render_template('indexView.html', lista=lista_atividades)
#
# @app.route('/listar-fichas')
# def getFichas():
#     lista_fichas = Academia().get_ficha()
#     return render_template('indexView.html', lista=lista_fichas)
#
# # @app.route('/home')
# # def getHome():
# #     return render_template('teste.html')
#
# @app.route('/cadastro-equipamento', methods=['GET', 'POST'])
# def cadastro_equipamento():
#     if request.method == 'POST':
#         nome = request.form.get('nome')
#         obs = request.form.get('observacao')
#         Academia().set_equipamentos(nome, obs)
#         return redirect(url_for('listar_equipamentos'))
#
#     if request.method == 'GET':
#         if request.args.get('id'):
#             print('id')
#         result = {'method': 'cadastro_equipamento'
#                   ,'title': 'Cadastrar equipamento'
#                   , 'group': [{'label': 'Nome'
#                               , 'placeholder': 'Digite o nome do equipamento'
#                               , 'name': 'nome'
#                               , 'value': ''
#                               , 'required': True},
#                               {'label': 'Observação'
#                               , 'placeholder': 'Campo de observação'
#                               , 'name': 'observacao'
#                               , 'value': ''
#                               , 'required': False}]}
#         return render_template('cadastro.html', element=result)
#
# @app.route('/cadastro-forma-pagamento', methods=['GET', 'POST'])
# def cadastro_forma_pagamento():
#     if request.method == 'POST':
#         nome = request.form.get('nome')
#         if request.args.get('id'):
#             Academia().update_forma_pagamento(request.args.get('id'), nome)
#         else:
#             Academia().set_forma_pagamento(nome)
#         return redirect(url_for('listar_forma_pagamento'))
#
#     if request.method == 'GET':
#         res = {'Id': '', 'Nome': ''}
#         if request.args.get('id'):
#             res = Academia().get_forma_pagamento_by_id(id=request.args.get('id'))
#         result = {'Id': res['Id']
#                   ,'method': 'cadastro_forma_pagamento'
#                   ,'title': 'Cadastrar forma de pagamento'
#                   , 'group': [{'label': 'Nome'
#                               , 'placeholder': 'Digite uma nova forma de pagamento'
#                               , 'name': 'nome'
#                               , 'value': res['Nome']
#                               , 'required': True}]}
#         return render_template('cadastro.html', element=result)
#
# @app.route('/listar-forma-pagamento')
# def listar_forma_pagamento():
#     result = Academia().get_forma_pagamento()
#     return render_template('index.html', lista=result)
#
# @app.route('/listar-equipamentos')
# def listar_equipamentos():
#     result = Academia().get_equipamento()
#     return render_template('index.html', lista=result)
#
# @app.route('/cadastro-forma-pagamento', methods=['GET', 'POST'])
# def update_forma_pagamento(id):
#     if request.method == 'POST':
#         nome = request.form.get('nome')
#         obs = request.form.get('observacao')
#         Academia().set_equipamentos(nome, obs)
#         return redirect(url_for('listar-forma-pagamento'))
#
#     if request.method == 'GET':
#         response = Academia().get_forma_pagamento_by_id(id)
#         result = {'method': 'cadastro-forma-pagamento/'+id
#                   , 'title': 'Editar equipamento '+id
#                   , 'group': [{'label': 'Nome'
#                               , 'placeholder': 'Digite a forma de pagamento'
#                               , 'value': response['Nome']
#                               , 'name': 'nome'
#                               , 'required': True}]}
#         return render_template('cadastro.html', element=result)
#
# @app.route('/delete_forma_pagamento')
# def delete_forma_pagamento():
#     if request.args.get('id'):
#         id = request.args.get('id')
#         Academia().delete_forma_pagamento(id)
#         return redirect(url_for('listar_forma_pagamento'))
#
# @app.route('/delete_equipamento')
# def delete_equipamento():
#     if request.args.get('id'):
#         id = request.args.get('id')
#         Academia().delete_equipamento(id)
#         return redirect(url_for('listar_equipamentos'))

if __name__ == '__main__':
    app.run(host='127.26.2.98', port=5000)

