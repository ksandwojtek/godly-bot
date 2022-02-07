#!/usr/bin/env python
import json
import aiohttp
from nextcord import Webhook
from bot.__main__ import *
from nextcord.ext import commands
import nextcord
import os
import validators
import sys
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))


class Nitro(commands.Cog):
    def __init__(self, client):
        self.client = client

    config = get_config()

    @commands.command()
    @commands.has_any_role(config["admin"])
    async def nitro(self, ctx):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(
                self.config["webhooks"]["nitro"], session=session)

            embedVar = nextcord.Embed(
                title="**Discord Nitro**", color=0xd084d4)
            embedVar.add_field(name=f"<:price_pi:933851518258516008>{categ}Pricing",
                               value=f"{tab}Nitro Classic 1 Year - **20€**\n{tab}Nitro Boost 1 Year - **35€**", inline=False)
            embedVar.add_field(
                name=f"<:info_pi:933851517855891527>{categ}Information", value=f"{tab}You know what Nitro is.", inline=False)
            file = nextcord.File("./assets/imgs/nitro.png")
            embedVar.set_image(url="attachment://nitro.png")

            await webhook.send(embed=embedVar, file=file, username="Discord Nitro")


def setup(client):
    filename = os.path.basename(__file__)[:-3]
    if validators.url(webhook_check(filename)):
        if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
            asyncio.set_event_loop_policy(
                asyncio.WindowsSelectorEventLoopPolicy())
        if asyncio.run(webhook_url_check(webhook_check(filename))) is True:
            client.add_cog(Nitro(client))

            logging_switch(filename)
    else:
        logging.error(f"{filename.capitalize()} webhook not found!")
