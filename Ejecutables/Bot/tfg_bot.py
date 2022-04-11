# -*- coding: utf-8 -*-
"""
This Example will show you how to use register_next_step handler.
"""
import telebot
import requests

from telebot import types

from Bot.configurationBot.botConfig import salas, operaciones, API_TOKEN, URL_NGROK

bot = telebot.TeleBot(API_TOKEN)
request_dict = {}

bot = telebot.TeleBot(API_TOKEN)

class Request:
    def __init__(self, name):
        self.name = name
        self.sala = ""
        self.indexSala = -1
        self.operation = None

# Handle '/start' and '/help'
@bot.message_handler(commands=['ayuda',
                               'inicio',
                               'hola'])
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
        user = request_dict[chat_id]

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        for operacion in operaciones:
            markup.add(operacion.name)

        msg = bot.reply_to(message, 'Bienvenido ' + user.name + '\n ¿Que operación quieres realizar?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_operation_step)

    except Exception as e:
        bot.reply_to(message, 'Ha habido un error al recoger la operación \n' + str(e))

def process_operation_step(message):
    try:
        chat_id = message.chat.id
        operation = message.text
        user = request_dict[chat_id]
        index = searchOperation(operation)
        if index != -1:
            user.operation = operaciones[index]

            if (user.operation.showKeyboard):
                markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
                for sala in salas:
                    markup.add(sala)

                msg = bot.reply_to(message, 'Operación seleccionada ' + operation + '\n ¿De que sala quieres información?',
                                   reply_markup=markup)
                bot.register_next_step_handler(msg, process_sala_step)

            else:
                sendReponse(message, user)

        else:
            raise Exception("Operación NO reconocida")

    except Exception as e:
        bot.reply_to(message, 'Ha habido un error al recoger el nombre')

def process_sala_step(message):
    try:
        chat_id = message.chat.id
        sala = message.text
        user = request_dict[chat_id]

        if sala in salas:
            indexSala = salas.index(sala)
            user.sala = sala
            user.indexSala = indexSala

            sendReponse(message, user)
        else:
            raise Exception("Sala no reconocida")

    except Exception as e:
        bot.reply_to(message, 'Ha habido un error al recoger la sala \n' + str(e))

def sendReponse(message, user):
    url = ""
    if (user.operation.showKeyboard) :
        url = URL_NGROK + "/" + user.operation.oppathlist + "?id=" + str(user.indexSala)
    else:
        url = URL_NGROK + "/" + user.operation.oppathlist

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

def searchOperation (nameoperation):
    for i in range(len(operaciones)):
        if operaciones[i].name == nameoperation:
            return i
    return -1

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

bot.infinity_polling()
