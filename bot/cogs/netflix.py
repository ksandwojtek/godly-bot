#!/usr/bin/env python
from tkinter import NE
import aiohttp
from nextcord import Webhook
import json
from bot.__main__ import *
from nextcord.ext import commands
import nextcord
import os
import validators
import sys
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))


class Netflix(commands.Cog):
    def __init__(self, client):
        self.client = client

    config = get_config()

    @commands.command()
    @commands.has_any_role(config["admin"])
    async def netflix(self, ctx):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(
                self.config["webhooks"]["netflix"], session=session)

            embedVar = nextcord.Embed(title="**Netflix**", color=0xe40414)
            embedVar.add_field(name=f"<:price_n:933876705402167347>{categ}Pricing",
                               value=f"{tab}Netflix random account - **10€**\n{tab}Netflix carded account - **30€**", inline=False)
            embedVar.add_field(name=f"<:info_n:933876704479436800>{categ}Information", value=f"{tab}Netflix random account - Cheaper Netflix subscription on a random {tab}account. Warranty 1 Month guaranteed *can go up to years if lucky*\n\n{tab}Netflix carded account - 10€ more for a 4k UHD subscription where {tab}you get a dedicated mail and password for you and the people you {tab}share the account with. Lifetime warranty if as long as carding {tab}{tab}method on it works. *Password change disables your Warranty.*", inline=False)
            file = nextcord.File("./assets/imgs/netflix.png")
            embedVar.set_image(url="attachment://netflix.png")

            await webhook.send(embed=embedVar, file=file, username="Netflix")


def setup(client):
    filename = os.path.basename(__file__)[:-3]
    if validators.url(webhook_check(filename)):
        if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
            asyncio.set_event_loop_policy(
                asyncio.WindowsSelectorEventLoopPolicy())
        if asyncio.run(webhook_url_check(webhook_check(filename))) is True:
            client.add_cog(Netflix(client))

            logging_switch(filename)
    else:
        logging.error(f"{filename.capitalize()} webhook not found!")
