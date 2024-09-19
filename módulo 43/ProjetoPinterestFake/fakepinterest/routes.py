#Aqui ficarão as rotas do nosso site# (links)
from flask import Flask, render_template, url_for, redirect 
from fakepinterest import app, database, bcrypt
from flask_login import login_required, login_user, logout_user
from fakepinterest.forms import FormLogin, FormCriarConta
from fakepinterest.models import Usuario, Foto




@app.route('/', methods = ["get", "Post"])
def homepage():
     formlogin = FormLogin()
     return render_template("homepage.html", form= formlogin) # essas informações devem estar entre aspas duplas

@app.route("/criarconta",  methods = ["get", "Post"])
def criarconta():
     formcriarconta = FormCriarConta()
     if formcriarconta.validate_on_submit():
          senha = bcrypt.generate_password_hash(formcriarconta.senha.data)
          usuario = Usuario(username = formcriarconta.username.data, senha = senha, email = formcriarconta.email.data )
          database.session.add(usuario)
          database.session.commit()
          login_user(usuario, remember = True)

          return redirect(url_for("perfil", usuario = usuario.username))

     return render_template("criarconta.html", form = formcriarconta) 


@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
     return render_template("perfil.html", idade = 23)