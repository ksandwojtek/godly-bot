#!/usr/bin/env python
import os
from bot.bot import Bot
import json
from bot.constants import TOKEN



def get_config():
    with open("config.json") as file:
        config = json.load(file)

    return config

def load_cogs():
    print('Loading cogs...')
    for fn in os.listdir("./bot/cogs"):
        if not fn.startswith("__"):
            if fn.endswith(".py"):
                print(f"Loading {fn}...")
                client.load_extension(f"bot.cogs.{fn[:-3]}")


def main():
    global client
    global tab, categ
    categ = "  "
    tab =  "⠀⠀⠀ "

    client = Bot()

    load_cogs()

    client.run(TOKEN)

if __name__ == '__main__':
    main()
