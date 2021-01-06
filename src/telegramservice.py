from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Available Commands:\n/register : register for zealios v2 stock notifications")


def stop(update, context):
    with open("users.json", "r") as file_users:
        users = json.load(file_users)
        file_users.close()

    chat_id = str(update.effective_chat.id)

    if chat_id in users["user_list"]:
        users["user_list"].remove(chat_id)
        with open("users.json", "w") as file_users:
            json.dump(users, file_users, indent=4)
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="You will no longer receive notifications.")
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="You are not registered!")


def register(update, context):
    try:

        with open("users.json", "r") as file_users:
            users = json.load(file_users)
            file_users.close()

        chat_id = str(update.effective_chat.id)

        if not chat_id in users["user_list"]:
            with open("users.json", "w") as file_users:
                users["user_list"].append(chat_id)
                json.dump(users, file_users, indent=4)
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Your registration was successful.")
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="You are already registered!")

    except:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="error")


def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Unknown command.")


class telegram_service:
    telegram_key = ""

    def __init__(self, api_key, debug=False):
        telegram_key = api_key
        updater = Updater(token=telegram_key, use_context=True)
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler('start', start))
        dispatcher.add_handler(CommandHandler('register', register))
        dispatcher.add_handler(CommandHandler('stop', stop))
        dispatcher.add_handler(MessageHandler(Filters.command, unknown))

        updater.start_polling()
