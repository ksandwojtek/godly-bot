#!/usr/bin/env python
from nextcord.ext import commands
import nextcord
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from bot.__main__ import *
import json
from nextcord import Webhook
import aiohttp

class Netflix(commands.Cog):
    def __init__(self, client):
        self.client = client

    config = get_config()

    @commands.command()
    @commands.has_any_role(config["admin"])
    async def netflix(self, ctx):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url('https://discord.com/api/webhooks/933875559220510741/wF0SqiqFMzma9-JdIXUM991crurzsd7BSxVuysqCofXLFyiHF5gd4H2OhNJId_aCBvYw', session=session)
        
            embedVar = nextcord.Embed(title = "**Netflix**", color = 0xe40414)
            embedVar.add_field(name = f"<:price_n:933876705402167347>{categ}Pricing", value = f"{tab}Netflix random account - **10€**\n{tab}Netflix carded account - **30€**", inline = False)
            embedVar.add_field(name = f"<:info_n:933876704479436800>{categ}Information", value = f"{tab}Netflix random account - Cheaper Netflix subscription on a random {tab}account. Warranty 1 Month guaranteed *can go up to years if lucky*\n\n{tab}Netflix carded account - 10€ more for a 4k UHD subscription where {tab}you get a dedicated mail and password for you and the people you {tab}share the account with. Lifetime warranty if as long as carding {tab}{tab}method on it works. *Password change disables your Warranty.*", inline = False)
            file = nextcord.File("./assets/imgs/netflix.png")
            embedVar.set_image(url = "attachment://netflix.png")

            await webhook.send(embed = embedVar, file = file, username = "Netflix")

def setup(client):
    client.add_cog(Netflix(client))