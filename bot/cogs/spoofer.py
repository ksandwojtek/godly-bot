#!/usr/bin/env python
from nextcord.ext import commands
import nextcord
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from bot.__main__ import *
from nextcord import Webhook
import aiohttp

class Spoofer(commands.Cog):
    def __init__(self, client):
        self.client = client

    config = get_config()

    @commands.command()
    @commands.has_any_role(config["admin"])
    async def spoofer(self, ctx):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url('https://discord.com/api/webhooks/933881458169348147/zVFLE9d6l3WqcO8pwpSiqT7MjP58h1m09EIu6ZEQP_dqY7_t89XculzXiWZIlRel01za', session=session)
        
            embedVar = nextcord.Embed(title = "**EAC/BE Spoofer**", color = 0x4B0082)
            embedVar.add_field(name = f"<:price_p:933844634327711815>{categ}Pricing", value = f"{tab}Spoofer 1 week - **10€**\n{tab}Spoofer 1 month - **25€**\n{tab}Spoofer lifetime - **45€**", inline = False)
            embedVar.add_field(name = f"<:info_p:933844633761497121>{categ}Information", value = f"{tab}Fully EAC and BE game supporting Spoofer\n{tab}{categ}- Not opensource pasted drivers or mappers for extra security.\n{tab}{categ}- Regular updates included.\n{tab}{categ}- *Advanced cleaner inside.*", inline = False)
        #  file = nextcord.File("./imgs/spoofer.png")
        #  embedVar.set_image(url = "attachment://spoofer.png")

            await webhook.send(embed = embedVar, username = "Spoofer")

def setup(client):
    client.add_cog(Spoofer(client))