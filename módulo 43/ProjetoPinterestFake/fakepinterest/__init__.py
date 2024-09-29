# Local para a criação do nosso app, banco de dados e tudo mais#

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from flask_bcrypt import Bcrypt  

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "f9bf78b9a18ce6d46a0cd2b0b86df9da" 
database = SQLAlchemy(app) 

app.config["UPLOAD_FOLDER"] = "static/fotos_post"


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = "homepage" 

from fakepinterest import routes