
from flask import Flask, render_template, url_for #o url_for permite usar o nome da função como diretório da página e não mais a direção informada no route pois podemos em algum momento querer mudar, no caso da função não tem porque essa mudança


app = Flask(__name__) 




@app.route("/") 
def homepage(): 
    return render_template("homepage.html")



# Agora imagina se tivessemso que criar esse perfil de usuário para todos os usuários, se tivessemos por exemplo 1000 usuários teriámos muitas dificuldades nosso. logo, temos de fazer isso tornar-se algo dinâmico e que se altere para cada um dos usuários porém mantendo a mesma estrutura que os demais.


@app.route("/perfil/<usuario>") # para tal devemos por o nome usuário logo após uma barra e o mesmo dento de tags <usuári> a mesma dis que isso é variável, da mesma forma faremos para a função que a acompanha só que sem as tags
def perfil(usuario): # agora a funão que exibe um perfil na tela é a função usuário. para que a mesma seja carregada em seu template é só adicionala a ele 
    return render_template("perfil.html", usuario = usuario, idade = 25)# isso me permite passar parãmetros para o meu html onde irei conseguir fazer cahamdas com o python dentro do própio html. para informações passadas aqui

# Dessa forma mesmo que você tenha um milhão de usuário, os mesmos terão seu próprio perfil com suas inoformações

if __name__ == "__main__":
    app.run(debug= True) 
    

   