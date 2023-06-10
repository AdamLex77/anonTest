from database import DataBase
from info import *
import telebot
from telebot import types
import config


bot = telebot.TeleBot(f'{config.bot_token}')
record = DataBase()

@bot.message_handler(content_types=['text'])
def age(message):
    if message == "/setinfo":
        bot.send_message(message.from_user.id, "how old are you?")
        bot.register_next_step_handler(message, domisili)        
            
def domisili(message):
    user_id = message.from_user.id
    
    age_user = message.text
    if not age_user.isdigit():
        bot.send_message(message.from_user.id, "_Gunakan angka, Bukan Huruf!!_", parse_mode="markdown")
        bot.register_next_step_handler(message, domisili)
        return

    new_data = {"old": {age_user}}
    record.update(user_id, new_data)

    bot.send_message(message.from_user.id, "where you from?")
    
    bot.register_next_step_handler(message, domisili)


def lol(message):
    user_id = message.from_user.id
    dom = message.text
    new_data = {"domisili": {dom}}
    record.update(user_id, new_data)

    data = record.search(user_id)

    my_gender = data.get("gender")
    partner_gender = data.get("partner_gender")
    my_old = data.get("old")
    my_dom = data.get("domisili")
    my_name = data.get("name")

    bot.send_message(message.from_user.id, f"Your name: {my_name}\nyour age: {my_old}\nyour domisili: {my_dom}\n\nEdit your gender or your partner's gender\nyou: {my_gender}\npartner: {partner_gender}")
