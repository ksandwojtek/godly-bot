#!/usr/bin/env python
from cmath import log
import os
import json

def nextcord_check():
    try:
        global nextcord

        import nextcord
    except ImportError:
        logging.error("Nextcord not found")
        os.system(f"cd {os.getcwd()}")
        os.system(f"py -m pip install -r requirements.txt")
        print("Nextcord installed. Run the bot again")
        exit()

def open_config():
    with open("config.json", "r") as file:
        config = json.load(file)
        return config

def config_check():
    try:

            if open_config()["token"].lower() in ["token", "", " "] or open_config()["prefix"].lower() in ["prefix", "", " "] or open_config()["guild"] in ["guild", "", " "] or open_config()["admin"] in ["admin", "", " "]:
                print("Opening config window")
                os.system("py configsetup.py")
                exit()
    except FileNotFoundError:
        logging.error("Config file not found")
        exit()


def main():
    global logging
    import logging

    if open_config()["debug"] is True:
        logger = logging.getLogger('nextcord')
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(filename='nextcord.log', encoding='utf-8', mode='w')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)

    level = logging.INFO
    fmt = '[%(asctime)s] [%(levelname)s] - %(message)s'
    logging.basicConfig(level=level, format=fmt)

    config_check()
    nextcord_check()

    try:
        from bot import __main__
    except ImportError:
        logging.error("Main file not found")

    __main__.main()

if __name__ == '__main__':
    main()
