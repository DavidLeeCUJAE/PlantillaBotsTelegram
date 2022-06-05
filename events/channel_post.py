#Importar librerias
import requests
import json
import os
from flask import Flask, request# Add your telegram token as environment variable
#Importar mis librerías de variables
from Datos import inline_button, keyboard, general_data

def get(i): #datos generales que aparecen en todos los message
  id_mensaje = i["message_id"]
  id_chat = i["chat"]["id"]
  nombre = i["chat"]["title"]
  return id_mensaje, id_chat, nombre

def text(i):
  id_mensaje, id_chat, nombre = get(i)
  texto = i["text"]
  print(texto + " en el canal " + nombre)

def sticker(i):
  id_mensaje, id_chat, nombre = get(i)
  sticker = i['sticker']
  print('Un sticker en el canal ' + nombre + ' con id: ' + sticker['file_id'])

def document(i):
    id_mensaje, id_chat, nombre = get(i)
    document = i['document']
    print('Un documento en el canal ' + nombre + ' con id: ' + document['file_id'])

def photo(i):
    id_mensaje, id_chat, nombre = get(i)
    photo1 = i['photo'](1)
    print('Una foto en el canal ' + nombre + ' con id: ' + photo1['file_id'])
