#Aqui ficarão as rotas do nosso site# (links)
from flask import render_template, url_for, redirect # adicionamos ao nosso flask o nosso redirect para redirecionamentos 
from fakepinterest import app, database, bcrypt #importamos o nosso banco de dados e o nosso bcrypt, no primeiro caso precisamos de acesso ao banco de dados e no segundo caso precisamos fazer a criptografia da nossa senha
from flask_login import login_required, login_user, logout_user #fizemos a importação so login_user e logout_user
from fakepinterest.forms import FormLogin, FormCriarConta 
from fakepinterest.models import Usuario, Foto #Fazemos a importação da classe Usuario e Foto do nosso models




@app.route('/', methods = ["get", "Post"])
def homepage():
     formlogin = FormLogin()
     return render_template("homepage.html", form= formlogin)




@app.route("/criarconta",  methods = ["GET", "POST"]) 
def criarconta():
     formcriarconta = FormCriarConta()
     if formcriarconta.validate_on_submit(): # primeiro verificamos se o nosso botão de submit foi apertado, e todos os valores estiverem validos, eles serão passados para o nosso banco de dados, se não, o usuário será direcionado ao criar conta para o formulário novamente
          senha = bcrypt.generate_password_hash(formcriarconta.senha.data) # A senha passada pelo formulário foi criptografada e adicionada a variável senha, quando formos passar a senha para a tabela, usaremos apenas essa variável já que sua origem fá foi passada por aqui.

          usuario = Usuario(email = formcriarconta.email.data, username = formcriarconta.username.data,senha = senha)#Aqui passamos todos os valores das colunas da tabela usuário, ou seja: o username que será igual ao username do formulário formcriarconta, a senha

          database.session.add(usuario)# vamos abrir uam seçáo no nosso banco de dados e passarei as informações da tabela usuário
          database.session.commit(usuario)#Vamos comitar essas informações no nosso banco de dados
          
          login_user(usuario, remember = True)# esse remember true é para que o usuário ainda está logado caso o mesmo deixe essa janela aberta 

          return redirect(url_for("perfil", usuario = usuario.username)) # Se estiver tudo ok com  opreenchimento do formulário o nosso o usuário será direcionado ao perfil do usuário onde a variável usuário será igual ao username  correspondente na tabela usuário

     return render_template("criarconta.html", form = formcriarconta) 

@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
     return render_template("perfil.html", idade = 23)