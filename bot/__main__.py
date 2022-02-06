#!/usr/bin/env python
import os
from bot.bot import Bot
import json
from bot.constants import TOKEN
import logging
import aiohttp
import asyncio


def webhook_check(str):
    with open("config.json", "r") as file:
        config = json.load(file)
        webhooks = config["webhooks"]
        return webhooks[str]


async def webhook_url_check(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 401:
                return False
            else:
                return True


def get_config():
    with open("config.json") as file:
        config = json.load(file)

    return config


def load_cogs():
    logging.getLogger().setLevel(logging.INFO)
    logging.info('Loading cogs...')
    logging.getLogger().setLevel(logging.ERROR)
    for fn in os.listdir("./bot/cogs"):
        if not fn.startswith("__"):
            if fn.endswith(".py"):
                client.load_extension(f"bot.cogs.{fn[:-3]}")


def logging_switch(fname: str):
    logging.getLogger().setLevel(logging.INFO)
    logging.info(f"Cog loaded: {fname.capitalize()}")
    logging.getLogger().setLevel(logging.ERROR)


def main():
    global client
    global tab, categ
    categ = "  "
    tab = "⠀⠀⠀ "

    client = Bot()

    load_cogs()

    client.run(TOKEN)


main()
