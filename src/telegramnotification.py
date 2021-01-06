import urllib.request
from bs4 import BeautifulSoup
import json
import telegram
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


class user_notificator(object):
    telegram_key = ""

    def get_users(self):
        try:
            open("users.json", "r")
        except FileNotFoundError:
            with open("users.json", "w") as file:
                file.write("{\"user_list\":[]}")
                file.close()

        with open("users.json", "r") as file_users:
            users = json.load(file_users)
            file_users.close()
            return users["user_list"]

    def send_to_all_users(self, key, message):
        bot = telegram.Bot(token=key)
        users = self.get_users()
        for user in users:
            bot.send_message(user, message)

    def __init__(self, api_key):
        telegram_key = api_key


class stock_checker(object):
    telegram_key = ""
    my_debug = False

    def zealios2_check(self):
        url = "https://candykeys.com/product/zealios-switches-v2"
        product_page = urllib.request.urlopen(url).read().decode("utf-8")
        parsed_page = BeautifulSoup(product_page, "html.parser")

        # danger ^= product not in stock
        zealios_list = parsed_page.find_all("span", class_="danger")
        return (len(zealios_list) != 6)

    def send_notifications(self, key, i_debug=False):
        if self.zealios2_check():
            msg = "Zealios V2 are in stock! https://candykeys.com/product/zealios-switches-v2"
            user_notificator(key).send_to_all_users(msg)

        else:
            if i_debug:
                msg = "DEBUG: not in stock"
                user_notificator(key).send_to_all_users(key, msg)

    def __init__(self, api_key, i_debug=False):
        telegram_key = api_key
        my_debug = i_debug
        pass
