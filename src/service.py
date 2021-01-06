import asyncio
from time import sleep
import sys
import signal
import json
import os
import logging

from telegramservice import telegram_service
from telegramnotification import stock_checker

telegram_key = ""
debug = False


async def async_telegram_service(api_key, i_debug=False):
    service = telegram_service(api_key, i_debug)


async def async_candykeys_checker(api_key, i_debug=False):
    checker = stock_checker(api_key, i_debug)
    checker.send_notifications(api_key, i_debug)


def sigterm_handler(_signo, _stack_frame):
    # Raises SystemExit(0):
    sys.exit(0)

def get_module_logger(mod_name):
    """
    To use this, do logger = get_module_logger(__name__)
    """
    logger = logging.getLogger(mod_name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s [%(name)-12s] %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

signal.signal(signal.SIGTERM, sigterm_handler)

# Load config
# with open("config.json", "r") as file_config:
#     config = json.load(file_config)
#     file_config.close()

#     telegram_key = config["api_key"]
#     debug = config["debug"]

# except IOError:
#     print("Config file does not exist!")

try:
    API_TOKEN = str(
        os.getenv('API_TOKEN', ''))
    DEBUG = str(os.getenv('DEBUG', ''))

    if (DEBUG == 'True'):
        DEBUG = True
    else:
        DEBUG = False

    asyncio.run(async_telegram_service(API_TOKEN, DEBUG))
    while True:
        print("Checking stock...")
        asyncio.run(async_candykeys_checker(API_TOKEN, DEBUG))
        sleep(10)

except Exception as e:
    get_module_logger(__name__).error("An Error occurred: " + e.message)


finally:
    print("Goodbye")
