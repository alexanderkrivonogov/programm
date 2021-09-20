import json
from pprint import pprint

import requests
from bs4 import BeautifulSoup
from config import sign
import datetime


def sign_zodiak(name):
    if name not in sign:
        return 0
    else:
        url = f'https://horo.mail.ru/prediction/{sign[name][0]}/today/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        return soup, name


def group_message(name_zod):
    soup, name = sign_zodiak(name_zod)
    if not soup:
        return "Я не могу понять что ты хочешь напиши /help"
    else:
        quotes = soup.find_all('div', class_='article__item article__item_alignment_left article__item_html')
        gorosc = soup.find_all('h1', class_='hdr__inner')
        a = f'{datetime.datetime.now().strftime("%d.%m.%Y")}\n{gorosc[0].text}  {sign[name][1]}\n'

        for i in range(0, len(quotes)):
            qou = quotes[i].find_all('p')
            for j in qou:
                a += f"\n{j.text}"
        return a


# file = open('ids.txt', 'r', encoding='utf-8')
# file2 = open('names', 'r', encoding='utf-8')
# file3 = open('count', 'r', encoding='utf-8')
# file4 = open('desc2.txt', 'r', encoding='utf-8')
#
# ids = []
# names = []
# desc = []
# langs = []
# count_members = []
#
# url = 'https://telegros.ru/%D0%BA%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3-%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB%D0%BE%D0%B2/%D1%87%D0%B0%D1%82%D1%8B-telegram?start=260'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# quotes = soup.find_all('div', class_='description')
#
# for i in range(268):
#     langs.append("RU")
#
# for i in file:
#     ids.append(i[:-1])
#
# for i in file2:
#     names.append(i[:-1])
#
# for i in file3:
#     count_members.append(i[:-1])
#
# for i in file4:
#     desc.append(i[:-1])
# c = {}
# file.close()
# file2.close()
# file3.close()
# file4.close()
#
# for i in range(len(ids)):
#     c[i] = {
#         "id": f"@{ids[i]}",
#         "name": names[i],
#         "lang": langs[i],
#         "desc": desc[i],
#         "members": int(count_members[i]),
#         "type": "chat",
#     }
# for i in c:
#     print(c[i])
#
# f = open('chats.json', "w")
# i = 0
# f.write(f'{json.dumps(c, indent=2)}')
# f.close()
#
# print(langs)
# print(ids)
# print(names)
# print(count_members)
# print(desc)
# # print(str(str(i).split("</div>,")
