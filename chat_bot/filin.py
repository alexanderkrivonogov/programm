import telebot

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(content_types=['text'])
def get_message(message):
    bot.send_message(message.chat.id, f'Я повторяю за тобой: "{message.text}"')


bot.polling(none_stop=True)
