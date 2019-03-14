from flask import Flask , render_template
app = Flask (__name__)

@app.route("/form_atualizar_pessoa")
def atualizar():
    return render_template("form_atualizar_pessoa.html")


@app.route("/incluir_pessoa")
def incluir():
    return render_template("incluir_pessoa.html")

@app.route("/exibir_mensagem")
def exibir():
    return render_template("exibir_mensagem.html")

@app.route("/listar-pessoa")
def listar ():
    return render_template("listar-pessoa.html")

@app.route("/")
def listar_padrao():
    return render_template("listar-pessoa.html")

app.run()