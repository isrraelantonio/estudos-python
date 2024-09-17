#Aqui ficarão as rotas do nosso site# (links)
from flask import Flask, render_template, url_for
from fakepinterest import app

@app.route('/')
def homepage():
     return render_template("homepage.html") # essas informações devem estar entre aspas duplas
@app.route('/perfil/<usuario>')
def perfil(usuario):
     return render_template("perfil.html", idade = 23)