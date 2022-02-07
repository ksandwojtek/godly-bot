#!/usr/bin/env python
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


class Steam(commands.Cog):
    def __init__(self, client):
        self.client = client

    config = get_config()

    @commands.command()
    @commands.has_any_role(config["admin"])
    async def steam(self, ctx):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(
                self.config["webhooks"]["steam"], session=session)

            embedVar = nextcord.Embed(title="**Steam**", color=0x0a1c45)
            embedVar.add_field(name=f"<:price_s:933873653077143593>{categ}Pricing",
                               value=f"{tab}Steam LVL 5 + 9-Year-Badge - **35€**\n{tab}Steam LVL 6 + 10-Year-Badge - **35.50€**\n{tab}Steam LVL 6 + 11-Year-Badge - **36€**\n{tab}Steam LVL 7 + 12-Year-Badge - **36.50€**\n{tab}Steam LVL 7 + 13-Year-Badge - **37€**\n{tab}Steam LVL 8 + 14-Year-Badge - **38€**", inline=False)
            embedVar.add_field(name=f"<:info_s:933873652716433438>{categ}Information",
                               value=f"{tab}Steam LVL X + X-Year-Badge All the same, just modded steam {tab}{tab}accounts so you don't have to earn the badges. All of them have {tab}some games on them and can be used as main accounts. any game {tab}can be added to it.", inline=False)

            file = nextcord.File("./assets/imgs/steam.png")
            embedVar.set_image(url="attachment://steam.png")

            await webhook.send(embed=embedVar, file=file, username="Steam")


def setup(client):
    filename = os.path.basename(__file__)[:-3]
    if validators.url(webhook_check(filename)):
        if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
            asyncio.set_event_loop_policy(
                asyncio.WindowsSelectorEventLoopPolicy())
        if asyncio.run(webhook_url_check(webhook_check(filename))) is True:
            client.add_cog(Steam(client))

            logging_switch(filename)
    else:
        logging.error(f"{filename.capitalize()} webhook not found!")
