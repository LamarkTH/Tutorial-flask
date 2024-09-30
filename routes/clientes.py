from flask import Blueprint,render_template
from database.cliente import CLIENTES

#Estruturação das rotas dos clientes, o que cada pagina vai fazer
'''
    /clientes/ :metodo GET - Listar os clientes
    /clientes/ :metodo POST- inserir o cliente no servidor
    /cliente/new :metodo GET - renderizar(mostrar) dados para a tela do cliente
    /clientes/<id> :metodo GET obter dados de um cliente
    /clientes/<id>/edit :metodo GET - renderizar um forma=ulario para editar um cliente
    /clientes/<id>/update :metodo PUT- atualizar dados de um cliente
    /clientes/<id>/delete :metodo DELETE - deleta o registro do usuario
'''

cliente_route=Blueprint('cliente',__name__)

@cliente_route.route("/")
def listar_clientes():
    return render_template("lista_clientes.html",clientes= CLIENTES)

@cliente_route.route("/",methods=['POST'])
def inserir_clientes():
    pass

@cliente_route.route("/new")
def formulario_criar_cliente():
    # return "Ola mundo"
    return render_template("formulario_criar_cliente.html")

@cliente_route.route("/<int:cliente_id>")
def exibir_dados_do_cliente(cliente_id):
    return render_template("exibir_dados_do_cliente.html")

@cliente_route.route("/<int:cliente_id>/edit")
def editar_dados_do_cliente():
    return render_template("editar_dados_do_cliente.html")

@cliente_route.route("/<int:cliente_id>/update",methods=['PUT'])#<int:cliente_id>/update(Estudar melhor o funionamento desse metodo)
def atualizar_dados_do_cliente(cliente_id):#Obs : Metodo PUT não é aceito em um formulario
    return ola

@cliente_route.route("/<int:cliente_id>/delete",methods=['DELETE'])
def deletar_cliente(cliente_id):#Obs : Metodo DELETE não é aceito em um formulario
    return ola