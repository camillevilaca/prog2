from flask import Flask , render_template, request,redirect, session
from modelo import os
from peewee import*
from modelo import * 
app = Flask (__name__)
app.config["SECRET_KEY"] = "685547"
pessoas = []  
@app.route("/excluir_pessoa")
def excluir():
    if session["usuario"]:
    cpf = request.args.get("cpf")
    for p in pessoas:
        if p.cpf == cpf:
            pessoas.remove(p)
    return render_template("exibir_mensagem.html", mensagem="pessoa excluída")

@app.route("/incluir_pessoa")
def incluir():
    return render_template("incluir_pessoa.html")

@app.route("/exibir_mensagem")
def exibir():
    return render_template("exibir_mensagem.html")
    
@app.route("/cadastrar_pessoa")
def cadastrar():
    nome = request.args.get("nome")
    endereco = request.args.get ("endereco")
    cpf = request.argas.get("cpf")
    Pessoa.create(nome=nome,
                  endereco=endereco
                  cpf=cpf)
    return render_template ("exibir_mensagem.html", mensagem="cadastro concluído", pessoa=(nome,endereco,cpf))


@app.route("/listar-pessoa")
def listar ():
    return render_template("listar-pessoa.html", lista=Pessoa.select())

@app.route("/")
def listar_padrao():
    return render_template("listar-pessoa.html", geral=lista)

@app.route("/form_atualizar_pessoa")
def form_atualizar_pessoa():
    nome = request.args.get("nome")
    for Pessoa in lista:
        if nome == Pessoa.nome:
            return render_template("form_atualizar_pessoa.html", Pessoa = Pessoa)
        else:
            return "ERRO"

@app.route("/atualizar_pessoa")
def atualizar_pessoa():
   	cpf = request.args.get("cpf")
	for p in pessoas:
		if p.cpf == cpf:
			return render_template("form_alterar_pessoa.html", informacao=p)
	return "pessoa não encontrada"

@app.route("/form_login")
def form_login():
    return render_template("form_login.html")

@app.route ("/login")
def login():
    login = request.args.get ("login")
    senha = request.args.get ("senha")
    if login == "camille_vilaca" and senha =="123":
        session["user"] = login
        return render_template ("listar-pessoa.html")
    else:
        return "login/senha invalidos"

@app.route ("/logout")
def logout():
    session.pop("user")
    return render_template ("listar-pessoa.html")


app.config["SECRET_KEY"] = "ldjeoeoedkdoe"
app.run(debug= True, host= "0.0.0.0")

