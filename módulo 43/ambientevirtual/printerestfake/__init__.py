
# Aqui faremos a criação do nosso app de fato 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # Aqui fazemos a importação das nossas ferramentas para banco de dados.

app = Flask(__name__) 

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"#configuramos uma variável para o nosso banco de dados  e passamos a pasta que o mesmo será alocado. Essa pasta será criada automáticamente dentro do projeto

database = SQLAlchemy(app) # nesse caso criamos o nosso banco de dados e passamos como referencia de uso o nosso app

from printerestfake import route