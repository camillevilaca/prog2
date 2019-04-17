from flask import Flask, render_template, request
from prova_2 import Livros
app = Flask (__name__) 
livro = [Livros("A_Corte_de_Espinhos_e_Rosas","Sarah_J_Maas")]
@app.route ("/")
def iniciar():
    return render_template("listar-pessoa.html")
app.run(debug=True, host="0.0.0.0")