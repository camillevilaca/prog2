from flask import Flask,render_template,request
app= Flask(__name__)

class Pessoa():
    def __init__(self,nome,idade,nascimento,cpf):
        self.nome=nome
        self.idade=idade
        self.nascimento=nascimento
        self.cpf=cpf

lista=[Pessoa("Piske",17,"12/09/2001","123.124.213-20"), Pessoa("Ravi",17,"16/07/2001","432.234.987.01")]

@app.route("/")
def carai():
    return render_template("inicio.html")

@app.route("/addpessoa")
def caramba():
    return render_template("adicionarpessoa.html")



@app.route("/listapessoa_sem_add")
def caramb1():

    return render_template("listarpessoa.html", So_cara_foda= lista)

@app.route("/listapessoa")
def caramb2():

    nome= request.args.get("Nome")
    idade= request.args.get("Idade")
    nasci= request.args.get("Nascimento")
    cpf= request.args.get("Cpf")
    val=0
    # comparar cpfs
    while val==0:
        for pessoa in lista:
            if cpf == pessoa.cpf:
                return render_template("erro_add_pessoa.html")
        val=1
        
    lista.append(Pessoa(nome,int(idade),nasci,cpf))
    return caramb1()

@app.route("/deletepessoa")
def caramb3():

    cpf= request.args.get("Cpf")
    for pessoa in lista:
        if cpf== pessoa.cpf:
            lista.remove(pessoa)
            break
    return render_template("mensagem.html")


@app.route("/form_alterar")
def caramb4():

    cpf= request.args.get("Cpf")
    for pessoa in lista:
        if cpf== pessoa.cpf:
            return render_template("form_alterar.html", pessoa=pessoa)

@app.route("/alterar_pessoa")
def caramb5():

    nome= request.args.get("Nome")
    idade= request.args.get("Idade")
    nasci= request.args.get("Nascimento")
    cpf= request.args.get("Cpf")
    pessoa_alterada= Pessoa(nome,idade,nasci,cpf)
    for pessoa in range(len(lista)):
        if cpf== lista[pessoa].cpf:
            lista[pessoa]=pessoa_alterada
            return render_template("pessoa_alterada.html")



app.run(debug=True)
