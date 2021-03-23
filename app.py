#import os
import flask
import json
from flask import Flask,request, jsonify
from flask import render_template
import pycep_correios
import telebot

#app = Flask(__name__)

#@app.route('/')
#@app.route('/index/')
#def index():
#    return render_template('index.html')



#@app.route('/zipcode/<zipcode>') # http://localhost:5000/zipcode/60050111
#def validar_cep(zipcode):
#    '''Função valida de número de cep junto ao site dos Correios.
#        - Parâmetro: cep.
#        - Retorna: json com as infomações:
#            - Cep válidos: Logradouro/Nome; Bairro/Distrito; Localidade/UF; CEP.
#            - Inválidos: msn: "Cep inválido"
#    '''
#    try:
#        endereco = pycep_correios.get_address_from_cep(zipcode)
#        #exemplo: http://localhost:5000/Cep/60050220
#        res = endereco
#        return json.dumps(res, ensure_ascii=False).encode('utf8')
#        #return jsonify(endereco)#f'<h1>Cep {endereco}</h1>'
#    except:
#        res = f'zip code invalid.:{zipcode}.'
#        return json.dumps(res, ensure_ascii=False).encode('utf8')
#        #return jsonify(f'Cep inválido:{cep}.')

##teste localhost
#'''if __name__ == '__main__':
#    app.run(debug=True)'''#

## É necessário um token, obtido atráves do BotFather do próprio Telegram
token = "1720866154:AAF9dw56n4wgn4JW-eKCh5Ni0-VMjWUgFPs"
bot = telebot.TeleBot(token)

# Método de comando de saudação
@bot.message_handler(commands=["start"])
def start_message(message):
        bot.send_message(message.chat.id, "Saudações, meu consagrado!\nO que será hoje?", parse_mode='HTML')

# Método de comandos extras
@bot.message_handler(commands=["help", "ajuda", "SOS"])
def help_message(message):
        bot.reply_to(message, "Só mandar uma mensagem que eu respondo.", parse_mode='HTML')

# Método que lida com um tipo de conteúdo de mensagem enviada ao BOT
@bot.message_handler(content_types=["sticker", "pinned_message", "audio", "video", "voice"])
def type_message(message):
        bot.send_message(message.chat.id, "Só respondo a mensagens de texto ou <b>imagens</b> no momento", parse_mode='HTML')

# Método para recebimento de imagens
@bot.message_handler(content_types=["photo"])
def type_message(message):
        # Todos os métodos de envio de mensagem do bot retornam a mensagem, podendo ser atribuída a uma variável usada mais tarde
        resposta = bot.reply_to(message, "Processando imagem...", parse_mode='HTML')
        # Várias mensagens podem ser enviadas num mesmo handler
        bot.reply_to(resposta, "Pronto!", parse_mode='HTML')

# Método que responde a uma mensagem normal que contenha qualquer texto
@bot.message_handler(func=lambda message: True)
def text_message(message):
        # Aqui entraria o chamado à parte de processamento da mensagem em si
        bot.reply_to(message, message.text)



#teste heroku
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
