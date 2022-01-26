#!/usr/bin/env python
from nextcord.ext import commands
import nextcord
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from bot.__main__ import *
import json
from nextcord import Webhook
import aiohttp


class Nordvpn(commands.Cog):
    def __init__(self, client):
        self.client = client

    config = get_config()

    @commands.command()
    @commands.has_any_role(config["admin"])
    async def nordvpn(self, ctx):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url('https://discord.com/api/webhooks/933878271832105021/36NfkII_xY-T2z1DhqpdmVJuVzSu-TQn-rvd0mCs0GowdQKHzQreEU6UDbPGrMxFV8pl', session=session)
        
            embedVar = nextcord.Embed(title = "**Netflix**", color = 0x4884fc)
            embedVar.add_field(name = f"<:price_nv:933880035117498409>{categ}Pricing", value = f"{tab}NordVPN random account - **8€**\n{tab}NordVPN carded account - **16€**", inline = False)
            embedVar.add_field(name = f"<:info_nv:933880256815849522>{categ}Information", value = f"{tab}NordVPN random account - Account with some months of {tab}{tab}subscription on it, *has guaranteed +6 months*\n\n{tab}NordVPN carded account - Account with autorenewal subscription {tab}on it will last forever as long as password or any other wont be {tab}{tab}changed. (Warranty included when loyal buyer or booster.)", inline = False)
            file = nextcord.File("./assets/imgs/nordvpn.png")
            embedVar.set_image(url = "attachment://nordvpn.png")

            await webhook.send(embed = embedVar, file = file, username = "NordVpn")

def setup(client):
    client.add_cog(Nordvpn(client))