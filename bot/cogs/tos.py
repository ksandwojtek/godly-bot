#!/usr/bin/env python
from nextcord.ext import commands
import nextcord
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from bot.__main__ import *
from nextcord import Webhook
import aiohttp

class Tos(commands.Cog):
    def __init__(self, client):
        self.client = client

    config = get_config()

    @commands.command()
    @commands.has_any_role(config["admin"])
    async def tos(self, ctx):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url('https://discord.com/api/webhooks/933862198336434226/X47eBvCZSsBxlrERM8UkLMw-J1DydhvAtI_QhS6qL14SUq4gl86EY9Y2zuHbbVrG9YTv', session=session)

            embedVar = nextcord.Embed(title = "**Shop ToS**", description = "**1.** When the payment is confirmed, you automatically agree to the Shop ToS.\n\n**2.** <@921103030357725204> is the only one who can accept or deny any Payment.\n\n**3.** After your Order has been given out you are not permitted to ask for changes on this Product.\n\n**4.** There are no Refunds for buying something that doesn't work on your System after reading the Requirements.\n\n **5.** You need to pay first so your Order will get received.\n\n**6.** Sharing the Product is forbidden; applies to License, HWID or IP bound products.\n\n**7.** You are not allowed to resell anything from my shop if you are not a reseller.\n\n**8.** For more information about a product ask <@921103030357725204>.\n\n**9.** Asking for some % Sale is forbidden.\n\n**10.** Warranty only applies to Products i have control over it; If you are a Loyal buyer or Booster the Warranty applies to the whole Shop.\n\n**11.** Warranty only activates after leaving a vouch/review in <#931782186233905273>\n\n**12.** The ToS can change at any time, if that occurs you automatically accept the changes.", color = 0x4B0082)

            await webhook.send(embed = embedVar, username = "Shop ToS")

def setup(client):
    client.add_cog(Tos(client))