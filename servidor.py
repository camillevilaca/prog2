from flask import Flask , render_template, request
from modelo import Pessoa
app = Flask (__name__)
lista = [Pessoa("Maria_Carolina_Mestre_Vilaça","mcarolvilaca@bol.com.br"),
    Pessoa("Perly_Nobile_Mestre","perlymestre@gmail.com"),
    Pessoa("Isabelle_Vitoria_Mestre_Vilaça","isbellevilaca7@gmail.com")
    ]  
@app.route("/form_atualizar_pessoa")
def atualizar():
    return render_template("form_atualizar_pessoa.html")

@app.route("/excluir_pessoa")
def excluir():
    achou = None
    nome = request.args.get("nome")
    for p in lista:
        if p.nome == nome:
            achou = p
            break
    if achou != None:
        lista.remove(achou)
    return render_template("exibir_mensagem.html")

@app.route("/incluir_pessoa")
def incluir():
    return render_template("incluir_pessoa.html")

@app.route("/exibir_mensagem")
def exibir():
    return render_template("exibir_mensagem.html")
    
@app.route("/cadastrar_pessoa")
def cadastrar():
    nome = request.args.get("nome")
    email = request.args.get ("email")
    nova_pessoa = Pessoa(nome, email)
    lista.append (nova_pessoa)
    return render_template ("exibir_mensagem.html")

        
@app.route("/listar-pessoa")
def listar ():
    return render_template("listar-pessoa.html", geral=lista)

@app.route("/")
def listar_padrao():
    return render_template("listar-pessoa.html")

app.run(debug= True, host= "0.0.0.0")