#Plantilla para programar bots

#Importar librerias
import requests  
import json
import os
from flask import Flask, request# Add your telegram token as environment variable
#Importar mis librerías de variables
from data import inline_button, keyboard, general_data
#Importar módulos
from events import message, inline_query, edited_message, chat_join_request, callback_query, channel_post, chat_join_request, chat_member, chosen_inline_result, edited_channel_post, my_chat_member, poll, poll_answer, pre_checkout_query, shipping_query


def obtener_tipochat (idchat):
    #Tipos disponibles según la API de Telegram
    #private, group, supergroup or channel
    json_data = {
            "chat_id": idchat
    }
    message_url = general_data.URL + 'getChat'
    respuesta = requests.post(message_url, json_data)
    mensajes_js = respuesta.content.decode("utf8")
    chat = json.loads(mensajes_js)
    tipochat = chat["result"]["type"]
    
    return tipochat

ultima_id = 0
mantenimiento = False

app = Flask(__name__)

print("Bot Activo")

@app.route('/', methods=['POST'])
def main():
    global mantenimiento
    respuesta = request.json
    print(respuesta)
    
    if "message" in respuesta:
        i = respuesta["message"]
        if 'via_bot' in i:
            message.via_bot(i)
        if "text" in i:
            message.text(i)       
        elif "document" in i:
            message.document(i) 
        elif "photo" in i:
            message.photo(i)
        elif "video" in i:
            message.video(i)
        elif "new_chat_members" in i:
            message.new_chat_members(i)
            
    elif "edited_message" in respuesta:
        i = respuesta["edited_message"]
        if "text" in i:
            edited_message.text(i)
        elif "photo" in i:
            edited_message.photo(i)
        elif "document" in i:
            edited_message.document(i)
        elif "video" in i:
            edited_message.video(i)
            
    elif "channel_post" in respuesta:
        i = respuesta["channel_post"]
        id_chat = i["sender_chat"]["id"]
        id_mensaje = i["message_id"]
        if "text" in i:
            print("es un mensaje de texto en un canal")
        elif "document" in i:
            print("es un documento")
        elif "photo" in i:
            print("es una foto")
        elif "video" in i:
            print("es un video")
            
    elif "edited_channel_post" in respuesta:
        i = respuesta["edited_channel_post"]
        
    elif "inline_query" in respuesta:
        i = respuesta["inline_query"]
        inline_query.query(i)
        
    elif "chosen_inline_query" in respuesta:
        i = respuesta["chosen_inline_query"]
        
    elif "callback_query" in respuesta:
        i = respuesta["callback_query"]
        data = i["data"]
        id_privado = i["from"]["id"]
        nombre = i["from"]["first_name"]
        if "last_name" in i["from"]:
            nombre = nombre + " " + i["from"]["last_name"]
        if "username" in i["from"]:
            usuario = "@"+i["from"]["username"]
        else:
            usuario = None
        id_privado = i["message"]["chat"]["id"]
        
    elif "shipping_query" in respuesta:
        i = respuesta["shipping_query"]
        
    elif "pre_checkout_query" in respuesta:
        i = respuesta["pre_checkout_query"]
        
    elif "poll" in respuesta:
        i = respuesta["poll"]
        
    elif "poll_answer" in respuesta:
        i = respuesta["poll_answer"]
        
    elif "my_chat_member" in respuesta:
        i = respuesta["my_chat_member"]
        
    elif "chat_member" in respuesta:
        i = respuesta["chat_member"]
        
    elif "chat_join_request" in respuesta:
        i = respuesta["chat_join_request"]
      
    return ''      
      
if __name__ == '__main__':  
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 
