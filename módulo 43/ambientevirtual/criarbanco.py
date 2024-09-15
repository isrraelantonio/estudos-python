from printerestfake import database,app # importamos o banco de dados e o app do printerestfake

with app.app_context(): # Aqui dizemos que a criação do banco seguirá o contexto do passado pelo app
    database.create_all() # chamamos a criação do nosso banco de dados dentro do contexto passado acima