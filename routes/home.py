#Blue prints no flask : Servem para modularizar o codigo, agrupa varias paginas que possuem relção entre si a partir de suas rotas
from flask import Blueprint, render_template

home_route=Blueprint('home',__name__)#Nome da rota, nesse caso, a rota principal só vai ter uma rota.

@home_route.route('/')
def home():
    return  render_template("index.html")#Buscando o indexhtml na pasta templates
