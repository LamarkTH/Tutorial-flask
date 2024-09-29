from flask import Flask, url_for, render_template

app=Flask(__name__)#Inicialização e organização dos recursos

@app.route("/")
def ola_mundo():
    nome="Informações"
    informacoes=[
                 {"nome":"Thiago","sexo":"M","profissao":"TI"},
                 {"nome":"Ana","sexo":"F","profissao":"Prof"},
                 {"nome":"Thales","sexo":"M","profissao":"Caminhoneiro"}
                 ]
    sobre="Meu nomre é josè tenho asddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"
    return render_template("index.html",titulo=nome,lista=informacoes,sobre=sobre)


@app.route("/sobre")
def pagina_sobre():
    return render_template("paginasobre.html")


app.run(debug=True)#Modo desenvolvedor