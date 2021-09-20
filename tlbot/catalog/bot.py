from catalog.models import Category

import telebot

bot = telebot.TeleBot('981502050:AAEock7NMbNd3tUzDSk4e3ZEACDT3yXnJhk')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    categories = Category.objects.all()
    bot.send_message(message.from_user.id, f"{categories}")


# bot.polling(none_stop=True, interval=0)
bot.polling(True, 0, 30)
