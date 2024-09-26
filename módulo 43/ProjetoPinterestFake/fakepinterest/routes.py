#Aqui ficarão as rotas do nosso site# (links)
from flask import render_template, url_for, redirect
from fakepinterest import app, database, bcrypt 
from flask_login import login_required, login_user, logout_user, current_user 
from fakepinterest.forms import FormLogin, FormCriarConta, FormFoto
from fakepinterest.models import Usuario, Foto 




@app.route('/', methods = ["GET", "POST"])
def homepage(): 
     formlogin = FormLogin()
     if formlogin.validate_on_submit():  
          usuario = Usuario.query.filter_by(email = formlogin.email.data).first()
          if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data): 
               login_user(usuario) 
               return  redirect(url_for("perfil",  id_usuario = usuario.id)) # devemos dentro de login também fazer essas mudanças para um direcionamento apartir do login.
               

     return render_template("homepage.html", form= formlogin) 




@app.route("/criarconta",  methods = ["GET", "POST"]) 
def criarconta():
     formcriarconta = FormCriarConta() 
     if formcriarconta.validate_on_submit(): 
          senha = bcrypt.generate_password_hash(formcriarconta.senha.data)

          usuario = Usuario(email = formcriarconta.email.data, username = formcriarconta.username.data,senha = senha)
          database.session.add(usuario)
          database.session.commit()
          
          login_user(usuario, remember = True)
          return redirect(url_for("perfil", id_usuario = usuario.id)) # bo nossso redirecionamento estamos informando que o usuário não será mais selecionado pelo nome e sim pelo id, dentro da nossa tabela 
     return render_template("criarconta.html", form = formcriarconta)



@app.route("/perfil/<id_usuario>", methods = ["GET", "POST"]) # Nesse caso fizemos a mudança em relação a quem nos referimos quando estamos buscando acessar o nosso usuário para nossa página de perfil. nesse caso fazemos uso do id_usuario pois  o id do mesmo é o único valor que define o usuário como único.
@login_required  
def perfil(id_usuario):
     if int(id_usuario) == int(current_user.id): # estamos verificando se o usuário do perfil é o mesmo que está logado na conta agora pelo id
          # Nesse caso o usuário estará vendo o seu própio perfil
            form_foto = FormFoto()
            return render_template("perfil.html", usuario = current_user, form = form_foto) 
     else:
          # Nesse caso o usuário estará vendo o perfi de outro usuário.
          usuario = Usuario.query.get(int(id_usuario))
          return render_template("perfil.html",  idade = 25,usuario = usuario,  form = None) 




@app.route("/logout") 
@login_required 
def logout():
     logout_user()
     return redirect(url_for("homepage")) 