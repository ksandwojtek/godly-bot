#!/usr/bin/env python
import pathlib
import json

with open(pathlib.Path(__file__).parents[1] / "config.json", "r") as file:
    config = json.load(file)

PREFIX = config["prefix"]
TOKEN = config["token"]
GUILD = config["guild"]
ADMIN = config["admin"]
