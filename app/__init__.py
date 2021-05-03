import flask
from flask import request, jsonify


# App Setup
app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Temporary data for testing
usuarios = [
    {'id': 0,
     'nome': 'Rahul',
     'sobrenome': 'Juliato',
     'nascimento': '07/08/1986',
     'habilidade': 'Programar apis'},
    {'id': 1,
     'nome': 'Beto',
     'sobrenome': 'Juliato',
     'nascimento': '07/08/1955',
     'habilidade': 'Programar churrasco'},
    {'id': 2,
     'nome': 'Menini',
     'sobrenome': 'Piologui',
     'nascimento': '10/10/1982',
     'habilidade': 'Desenhi coisi legalzi'}
]


# Rotas
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def home():
    return "<h1>Título da API</h2><p>Esse site é uma micro API mínima protótipo.</p>"

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Recurso não encontrado.</p>", 404

@app.errorhandler(500)
def page_not_found(e):
    return "<h1>Erro</h1><p>Erro interno do servidor.</p>", 500

@app.route('/api/usuario/todos', methods=['GET'])
def api_all():
    return jsonify(usuarios)

@app.route('/api/usuario/', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "<h1>Erro</h1><p>ID não fornecida. Espeficique uma ID.</p>"

    results = []

    for book in usuarios:
        if book['id'] == id:
            results.append(usuarios[id])

    return jsonify(results)


# Run App
if __name__ == "__main__":
    app.run()
