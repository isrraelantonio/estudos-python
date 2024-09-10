
from flask import Flask, render_template #Aqui redenterizamos os arquivos dentro da nossa pasta templates, pois essa foi a forma que o flask encontrou de conseguir entender que o código deverá rodar uma home page para uma das páginas, logo, todas as páginas devem estar dentro do arquivo templates para que elas sejam encontradas e executadas.


app = Flask(__name__) 

@app.route("/")  # esssa esstrutura com o @ é um pouco diferente do que já vimos no python. o mesmo atribui funcionalidade a função abaixo, que ieremos fazer uso.Logo,  para criação de novos links sempre será necessário a criação desses dois em conjunto

def homepage(): 
    return render_template("homepage.html") # Agora chamando a função render_template e passando o nome do arquivo, conseguimos acessá-lo dentro da nossa página templates

@app.route("/perfil") # veja que para a criação do link para perfil do usuário seria necessária a criação de um route para o mesmo e também uma função para agregar valor para o mesmo, que no caso será a função perfil abaixo.

def perfil(): 
    return render_template("perfil.html") # Aqui por exemplo poderiamos cirar todo o conteúdo da página, porém isso deixaria o nosso código muito sujo e repleto de informações, que poderiam confundir a nossa cabeça.
    #Logo deveremos fazer essa criação externamente, dentro de uma pasta que daremos o nome de templates, e dentro da mesma crianriaremos os nossos arquivos do tipo html, para cada uma das nossas páginas dentro do nosso site.



if __name__ == "__main__":
    app.run(debug= True) 
    

   