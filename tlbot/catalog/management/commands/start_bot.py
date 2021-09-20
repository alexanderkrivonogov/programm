from django.core.management import BaseCommand
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from telegram_bot_pagination import InlineKeyboardPaginator
from catalog.models import Category, Product
import telebot

bot = telebot.TeleBot('981502050:AAEock7NMbNd3tUzDSk4e3ZEACDT3yXnJhk')


class Command(BaseCommand):
    help = "Телеграм бот"

    def handle(self, *args, **options):
        print('Bot started')
        bot.polling(True, 0, 30)

    @staticmethod
    @bot.message_handler(content_types=['text'])
    def unknown_message(message):
        Command.get_categories(message)

    @staticmethod
    @bot.callback_query_handler(func=lambda callback: callback.data == 'categories')
    def categories(callback):
        Command.get_categories(callback.message, edit=True) \

    @staticmethod
    @bot.callback_query_handler(func=lambda callback: callback.data == 'products')
    def products(callback):
        Command.get_products(callback.message)

    @staticmethod
    def get_categories(message, edit=False):
        keyboard = InlineKeyboardMarkup()

        for category in Category.objects.all():
            keyboard.add(
                *[InlineKeyboardButton(text=category.name, callback_data=f'category {category.id}')],
            )

        if edit:
            bot.edit_message_text(
                'Выберите категорию:',
                message.chat.id,
                message_id=message.message_id,
                reply_markup=keyboard,
            )
        else:
            bot.send_message(message.chat.id, 'Выберите категорию:', reply_markup=keyboard)

    @staticmethod
    @bot.callback_query_handler(func=lambda callback: callback.data.startswith('category'))
    def get_products(callback):
        category_id = callback.data.split()[-1]
        keyboard = InlineKeyboardMarkup()

        for product in Product.objects.filter(category_id=category_id):
            keyboard.add(
                *[InlineKeyboardButton(text=product.name, callback_data=f'product {product.id}')],
            )

        keyboard.add(InlineKeyboardButton(text='🔙 Назад', callback_data='categories'))
        if callback.message:
            bot.edit_message_text(
                'Выберите товар:',
                chat_id=callback.message.chat.id,
                message_id=callback.message.message_id,
                reply_markup=keyboard,
            )
