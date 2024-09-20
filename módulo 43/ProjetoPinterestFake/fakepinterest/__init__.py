# Local para a criação do nosso app, banco de dados e tudo mais#

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager  #faremos assim a importação desses puglins 
from flask_bcrypt import Bcrypt  

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "f9bf78b9a18ce6d46a0cd2b0b86df9da" # Nessa configurção do app definimos uma secret_key que vai tomar como exemplo essa construção para criptografar a senha do usuário. Então criamos uma chave gande como exemplo
database = SQLAlchemy(app) 

bcrypt = Bcrypt(app) #Aqui criaremos a vaariável que recebe essa função  e passamos como parâmetro o nosso app fazemos o mesmo com o login_manager
login_manager = LoginManager(app)

login_manager.login_view = "homepage" # Nesse caso definimos qual a página view que geencia o nosso login, ou seja se o usuário estiver logado para onde o mesmo será direcionado? para a nossa hoempage.

from fakepinterest import routes