# -*- coding: utf-8 -*-
"""
This Example will show you how to use register_next_step handler.
"""
import telebot
import requests

from telebot import types

API_TOKEN = '5260264151:AAFmQ04QpQJ-epSw22C_qOJP0Qhaf2GUAnw'

bot = telebot.TeleBot(API_TOKEN)
request_dict = {}

bot = telebot.TeleBot(API_TOKEN)

class Request:
    def __init__(self, name):
        self.name = name
        self.sala = None

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):

    msg = bot.reply_to(message, """\
Hola, ¿que tal?.
¿Cual es tu nombre?
""")

    bot.register_next_step_handler(msg, process_name_step)

def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = Request(name)
        request_dict[chat_id] = user

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Sala 1', 'Sala 2', 'Sala 3', 'Sala 4', 'Sala 5')

        msg = bot.reply_to(message, 'Bienvenido ' + user.name + '\n ¿De que sala quieres información?', reply_markup=markup)
        bot.register_next_step_handler(msg, sendReponse)
    except Exception as e:
        bot.reply_to(message, 'Ha habido un error al recoger el nombre')

def process_sala_step(message):
    try:
        chat_id = message.chat.id
        sala = message.text
        user = request_dict[chat_id]
        if (sala == u'Sala 1') or \
            (sala == u'Sala 2') or\
            (sala == u'Sala 3') or \
            (sala == u'Sala 4') or \
            (sala == u'Sala 5'):
            user.sala = sala
        else:
            raise Exception("Sala no reconocida")

        bot.send_message(chat_id, 'Usuario ' + user.name + '\n desea información sala:' + str(user.sala) + '\n')

    except Exception as e:
        bot.reply_to(message, 'Ha habido un error al recoger la sala')


def sendReponse(message):
    url = "http://dade-92-189-94-207.ngrok.io/sala?id=0"
    #querystring = {"country":"Denmark"}
    #headers = {
    #    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    #    'x-rapidapi-key': rapidapitoken}
    #response = requests.request("GET", url, headers=headers, params=querystring)
    response = requests.request("GET", url)

    #if not response.json()["error"]:
    bot.reply_to(message, str(response.json()))
    #else:
        #bot.reply_to(message, "Error: {!s} , StatusCode: {!s}, Message: {!s}".format(response.json()["error"], response.json()["statusCode"], response.json()["message"]))

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

bot.infinity_polling()
