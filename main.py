from flask import Flask
from flask import Blueprint
from routes.home import home_route
from routes.clientes import cliente_route


app=Flask(__name__)#Inicialização e organização dos recursos

#Todas as paginas relacionadas com a pagina home, ou seja, suas rotas tem que estar em um mesmo modulo
app.register_blueprint(home_route)#Registrando a rota home no arquivo principal.

#Todas as paginas relacionadas com a pagina clientes, ou seja, suas rotas tem que estar em um mesmo modulo
app.register_blueprint(cliente_route, url_prefix='/clientes')
#Registrando a rota home no arquivo principal.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
