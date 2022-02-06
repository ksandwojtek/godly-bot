#!/usr/bin/env python
from distutils.core import setup
import nextcord
from nextcord.ext import commands
import platform
import os
import sys
import re

from bot.constants import PREFIX

from _version import __version__

description = """
Made by ksndq#7595
"""


class Bot(commands.Bot):
    def __init__(self):

        intents = nextcord.Intents.all()
        self.prefix = PREFIX

        super().__init__(command_prefix=self.prefix, intents=intents,
                         help_command=None, pm_help=None, description=description)

    async def on_ready(self):
        print("-------------------")
        print(f"Loggined in as: {self.user.name}")
        print(f"Bot Version: { __version__}")
        print(f"Nextcord API Version: {nextcord.__version__}")
        print(f"Python Version: {platform.python_version()}")
        print(f"OS: {platform.system()} {platform.release()} ({os.name})")
        print("-------------------")
