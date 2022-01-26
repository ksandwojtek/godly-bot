#!/usr/bin/env python
from nextcord.ext import commands
import nextcord
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from bot.__main__ import *
from nextcord import Webhook
import aiohttp

class Spotify(commands.Cog):
    def __init__(self, client):
        self.client = client

    config = get_config()

    @commands.command()
    @commands.has_any_role(config["admin"])
    async def spotify(self, ctx):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url('https://discord.com/api/webhooks/933862164182220830/iws-wOA4qxkHsfVTlUssMsXLbi3ahTYmUPwlR0bjwJSowMikT3JJUNR8_kTNwTSdOx2T', session=session)
        
            embedVar = nextcord.Embed(title = "**Spotify**", color = 0x18d860)
            embedVar.add_field(name = f"<:price_l:933852732274663435>{categ}Pricing", value = f"{tab}Premium account - **5€**\n{tab}Lifetime premium on personal account - **20€**", inline = False)
            embedVar.add_field(name = f"<:info_l:933852732316594186>{categ}Information", value = f"{tab}**Premium account** - Random account with a premium upgrade on it {tab}where you can listen along to.\n\n{tab}**Lifetime premium on personal account** - Your personal account will {tab}get a lifetime premium upgrade, which is legit and you can listen to {tab}music without ads on your phone and PC and anything else you {tab}{tab}linked Spotify to, Lifetime warranty.", inline = False)
            file = nextcord.File("./assets/imgs/spotify.png")
            embedVar.set_image(url = "attachment://spotify.png")

            await webhook.send(embed = embedVar, file = file, username = "Spotify")

def setup(client):
    client.add_cog(Spotify(client))