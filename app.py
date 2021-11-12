import sqlite3
from flask import Flask, g

DATABASE = "blog.db"
SECRET_KEY = "minha_chave"

app = Flask(__name__) # Para criar o aplicativo
app.config.from_object(__name__)

def conectar_bd():
    return sqlite3.connect(DATABASE)

@app.before_request
def pre_requisicao():
    g.bd = conectar_bd()

@app.teardown_request
def pos_requisicao(exception):
    g.bd.close()

@app.route('/') # página raiz/principal do site/aplicativo
def exibir_entradas():
    sql = "SELECT titulo, texto FROM entradas ORDER BY id DESC"
    cur = g.bd.execute(sql)
    entradas = []
    for titulo, texto in cur.fetchall():
        entradas.append({'titulo': titulo, 'texto': texto})
    return str(entradas)


# @app.route('/') # página raiz do site
# def index():
#    return "Olá, pessoALL!! Bem-vindos!!! <a href='/pudim'> link</a>"

# @app.route('/pudim') # página pudim do site
# def pudim():
#    return "<h1 style='color:red;'>Só gosto de pudim mole.</h1>"
