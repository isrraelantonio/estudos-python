#Aqui ficarão os formulários do nosso site#
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError 
from fakepinterest.models import Usuario

class FormLogin(FlaskForm):
   email= StringField("Email", validators= [DataRequired(), Email()] )
   senha = PasswordField("senha", validators= [DataRequired()]) 
   botao =SubmitField("Fazer Login" )



class FormCriarConta(FlaskForm):
    email= StringField("E-mail", validators= [DataRequired(), Email()]) 
    username = StringField("Nome de Usuário", validators=[DataRequired()])
    senha = PasswordField("senha",validators= [DataRequired(), Length(6, 20)] ) 
    confirmacao_senha = PasswordField("Confirme a senha,", validators=[DataRequired(), EqualTo("senha")] )
    botao_confirmacao = SubmitField("Criar conta")



 

    def validate_email(self, email):
    
        usuario = Usuario.query.filter_by(email = email.data).first() 
        if usuario :
            return ValidationError("E-mail já cadastrado, faça login para continuar")
