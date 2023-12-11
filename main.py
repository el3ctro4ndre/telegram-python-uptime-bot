"""
Uptime telegram bot
Made by: @el3ctro4ndre
"""

import logging
from telegrampy.ext import commands
import requests
import time
import asyncio

async def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(message)s", datefmt="%H:%M:%S")

    class MyHelpCommand(commands.HelpCommand):
        async def send_bot_help(self):
            pass
        async def send_cog_help(self, cog):
            pass
        async def send_command_help(self, command):
            pass

    bot = commands.Bot("<TOKEN HERE>", help_command = MyHelpCommand()) ## PUT HERE YOUR TOKEN

    chat = await bot.get_chat(chat_id=<CHAT ID>) ## PUT HERE YOUR CHAT ID

    names =  ["Interface 1",         "Interface 2",       ] ## CHANGE NAME AND URL OF
    urls =   ["http://example.com/", "http://example.com/"] ## INTERFACES (ADD AS MANY)
    status = ["online",              "online",            ] ## AS YOU WANT

    logging.info("---------------------")
    logging.info("-- START OF LOGGER --")
    logging.info("---------------------")

    while True:
        for url in urls:
            index = urls.index(url)
            name = names[index]
            try:
                r = requests.get(url)
                logging.info(f"{name} online")
                if status[index] != "online":
                    await chat.send(f"🟢 | {name} online")
                    status[index] = "online"
    
            except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
                logging.info(f"{name} offline")
                if status[index] !=  "offline":
                    await chat.send(f"🔴 | {name} offline")
                    status[index] = "offline"
            
        logging.info("---------------------")

        time.sleep(120)

try:
    asyncio.run(main())

except (KeyboardInterrupt, asyncio.exceptions.CancelledError):
    logging.info("--- END OF LOGGER ---")
    logging.info("---------------------")
    logging.disable()