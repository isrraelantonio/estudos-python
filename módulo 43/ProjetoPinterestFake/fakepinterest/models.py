#Aqui ficarão  os nossos modelos de banco de dados#

from fakepinterest import database, login_manager
from flask_login import UserMixin 
from datetime import datetime
agora = datetime.now()


@login_manager.user_loader
def load_usuario(id_usuario): 
    return Usuario.query.get(int(id_usuario)) 


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key = True)
    username = database.Column(database.String, nullable = False)
    email = database.Column(database.String, nullable = False, unique = True)
    senha = database.Column(database.String, nullable = False)
    fotos = database.relationship("Foto", backref = "usuario", lazy = True)


class Foto(database.Model):
   id = database.Column(database.Integer, primary_key = True)
   imagem = database.Column(database.String, default= "default.png")
   data_criacao = database.Column(database.DateTime, nullable = False, default = agora.date())
   id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable = False)
