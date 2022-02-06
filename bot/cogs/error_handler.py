#!/usr/bin/env python
import logging
import aiohttp
from nextcord import Webhook
import json
from bot.__main__ import *
from nextcord.ext import commands
import nextcord
import os
import sys
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))


class Errorhandler(commands.Cog):
    def __init__(self, client):
        self.client = client

    config = get_config()

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.CommandNotFound):
            logging.error("Command not found")


def setup(client):
    client.add_cog(Errorhandler(client))
