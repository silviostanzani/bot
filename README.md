# bot

* app.py: Bot para telegram implementado em python

* Os arquivos a seguir são utilizados para fazer deploy do bot no Heroku:
  * Procfile : define como iniciar a aplicação
  * requirements.txt : pacotes necessários para fazer deploy (obtido do ambiente conda)
  * runtime.txt : versão do python para executar o script

* Comandos para colocar o bot no ar
  * heroku login
  * heroku create 
  * git push heroku main  
