#!/usr/bin/env python
from nextcord.ext import commands
import nextcord
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from bot.__main__ import *
from nextcord import Webhook
import aiohttp
import json

class Nitro(commands.Cog):
    def __init__(self, client):
        self.client = client

    config = get_config()

    @commands.command()
    @commands.has_any_role(config["admin"])
    async def nitro(self, ctx):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url('https://discord.com/api/webhooks/933862060977188944/sqojL1k3UJDkqbmXcC2h-DlgmCXGby_OdGcaROwX5Ao6NWpPtCz16CNrgNprXn88QsWd', session=session)
        
            embedVar = nextcord.Embed(title = "**Discord Nitro**", color = 0xd084d4)
            embedVar.add_field(name = f"<:price_pi:933851518258516008>{categ}Pricing", value = f"{tab}Nitro Classic 1 Year - **20€**\n{tab}Nitro Boost 1 Year - **35€**", inline = False)
            embedVar.add_field(name = f"<:info_pi:933851517855891527>{categ}Information", value = f"{tab}You know what Nitro is.", inline = False)
            file = nextcord.File("./assets/imgs/nitro.png")
            embedVar.set_image(url = "attachment://nitro.png")

            await webhook.send(embed = embedVar, file = file, username = "Discord Nitro")

def setup(client):
    client.add_cog(Nitro(client))