#!/usr/bin/env python
import aiohttp
from nextcord import Webhook
from bot.__main__ import *
from nextcord.ext import commands
import nextcord
import os
import sys
import validators
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))


class Spoofer(commands.Cog):
    def __init__(self, client):
        self.client = client

    config = get_config()

    @commands.command()
    @commands.has_any_role(config["admin"])
    async def spoofer(self, ctx):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(
                self.config["webhooks"]["spoofer"], session=session)

            embedVar = nextcord.Embed(
                title="**EAC/BE Spoofer**", color=0x4B0082)
            embedVar.add_field(name=f"<:price_p:933844634327711815>{categ}Pricing",
                               value=f"{tab}Spoofer 1 week - **10€**\n{tab}Spoofer 1 month - **25€**\n{tab}Spoofer lifetime - **45€**", inline=False)
            embedVar.add_field(name=f"<:info_p:933844633761497121>{categ}Information",
                               value=f"{tab}Fully EAC and BE game supporting Spoofer\n{tab}{categ}- Not opensource pasted drivers or mappers for extra security.\n{tab}{categ}- Regular updates included.\n{tab}{categ}- *Advanced cleaner inside.*", inline=False)
        #  file = nextcord.File("./imgs/spoofer.png")
        #  embedVar.set_image(url = "attachment://spoofer.png")

            await webhook.send(embed=embedVar, username="Spoofer")


def setup(client):
    filename = os.path.basename(__file__)[:-3]
    if validators.url(webhook_check(filename)):
        if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
            asyncio.set_event_loop_policy(
                asyncio.WindowsSelectorEventLoopPolicy())
        if asyncio.run(webhook_url_check(webhook_check(filename))) is True:
            client.add_cog(Spoofer(client))

            logging_switch(filename)
    else:
        logging.error(f"{filename.capitalize()} webhook not found!")
