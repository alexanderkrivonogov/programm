from telebot import TeleBot, types
from functions import group_message
from config import TOKEN, sign
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = TeleBot(TOKEN)


# @bot.message_handler(commands=['i'])
# def start_bot(message):
#     bot.send_message(message.from_user.id, f"Привет {message.chat.first_name}\n"
#                                            f"Я бот который расскажет тебе всё что с тобой случится за сегодня"
#                                            f"\nНапиши мне кто ты по знаку зодиака ) И я открою тебе тайну")
#
#
# @bot.message_handler(commands=["start"])
# def start(m):
#     name = ''
#     msg = bot.send_message(m.chat.id, "Вас приветствует Бот")
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(*[types.KeyboardButton(name.title()) for name in sign])
#     bot.send_message(m.chat.id, 'Выберите свой знак зодиака!',
#                      reply_markup=keyboard)
#
#
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text == "Привет":

#         bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Напиши мне, кто ты по знаку зодиака :)")
#     else:
#         print(message.chat.id, message.chat.username, message.text)
#         bot.send_message(message.chat.id, group_message(message.text.lower()))
#
#
# bot.polling(none_stop=True, interval=10)

@bot.message_handler(commands=['start'])
def unknown_message(message):

    get_categories(message)


@bot.message_handler(content_types=['text'])
def unknown_message(message):
    bot.delete_message(message.chat.id, message.message_id)


@bot.callback_query_handler(func=lambda callback: callback.data == 'categories')
def categories(callback):
    get_categories(callback.message, edit=True)


def get_categories(message, edit=False):
    keyboard = InlineKeyboardMarkup()
    print(message.chat.id, message.chat.username)
    for category in sign:
        keyboard.add(
            *[InlineKeyboardButton(text=category.title(), callback_data=f'{category}')],
        )
    if edit:
        bot.edit_message_text(
            'Выберите знак зодиака',
            message.chat.id,
            message_id=message.message_id,
            reply_markup=keyboard,
        )
    else:
        bot.send_message(message.chat.id, 'Выберите знак зодиака', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda callback: callback.data.startswith(''))
def get_products(callback):
    a = callback.data
    prod = group_message(a)
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text='🔙 Назад', callback_data='categories'))
    if callback.message:
        bot.edit_message_text(
            f'{prod}',
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            reply_markup=keyboard,
        )


bot.polling(none_stop=True)
