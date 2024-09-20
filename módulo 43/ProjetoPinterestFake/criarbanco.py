from  fakepinterest import database, app
from fakepinterest.models import Usuario, Foto
from sqlalchemy.dialects import mysql, mssql

with app.app_context():
    database.create_all()