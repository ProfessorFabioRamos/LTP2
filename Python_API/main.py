from flask import Flask,request,jsonify
app = Flask(__name__)

produtos = [
    {"id":1,"nome":"Espada","preco":100},
    {"id":2,"nome":"Escudo", "preco":150}
]

@app.route('/')
def home():
    return "Bem-vindo"

@app.route('/produto', methods=['GET'])
def get_produtos():
    return jsonify(produtos)

@app.route('/produto/<int:id>', methods=['GET'])
def get_produto(id):
    for p in produtos:
        if p["id"] == id:
            return jsonify(p)
    return jsonify({"erro":"produto nao encotrado"}),404

@app.route('/produto/',methods = ['POST'])
def adicionar_produto():
    novo = request.get_json()
    produtos.append(novo)
    return jsonify(novo),201

@app.route('/produto/<int:id>',methods=['PUT'])
def atualizar_produto(id):
    dados = request.get_json()
    for p in produtos:
        if p["id"]==id:
            p.update(dados)
            return jsonify(p)
    return jsonify({"erro":"Produto nao encontrado"}),404

@app.route('/produto/<int:id>',methods = ['DELETE'])
def deletar_produto(id):
    for p in produtos:
        if p["id"] == id:
            produtos.remove(p)
            return jsonify({"mensagem":"Produto Removido"})
    return jsonify({"erro":"Produto nao encontrado"}),404

if __name__=='__main__':
    app.run(debug=True)


# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "API online!"

# if __name__ == "__main__":
#     app.run(debug=True)
