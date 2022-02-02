#!/usr/bin/env python
from bot import __main__
import os
import json
with open("config.json", "r") as file:
    config = json.load(file)
    if config["token"].lower() in ["token", "", " "] or config["prefix"].lower() in ["prefix", "", " "] or config["guild"].lower() in ["guild", "", " "] or config["admin"].lower() in ["admin", "", " "]:
        print("Opening config window")
        os.system("py configsetup.py")
        exit()

try:
    import nextcord
except ImportError:
    print("Nextcord not found")
    os.system(f"cd {os.getcwd()}")
    os.system(f"py -m pip install -r requirements.txt")
    print("Nextcord installed. Run the bot again")
    exit()


__main__.main()
