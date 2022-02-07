#!/usr/bin/env python
import logging
import asyncio
import aiohttp
from nextcord import Webhook
from bot.__main__ import *
from nextcord.ext import commands
import nextcord
import validators
import os
import sys
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))


class Tos(commands.Cog):
    def __init__(self, client):
        self.client = client

    config = get_config()

    @commands.command()
    @commands.has_any_role(config["admin"])
    async def tos(self, ctx):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(
                self.config["webhooks"]["tos"], session=session)

            embedVar = nextcord.Embed(title="**Shop ToS**", description="**1.** When the payment is confirmed, you automatically agree to the Shop ToS.\n\n**2.** <@921103030357725204> is the only one who can accept or deny any Payment.\n\n**3.** After your Order has been given out you are not permitted to ask for changes on this Product.\n\n**4.** There are no Refunds for buying something that doesn't work on your System after reading the Requirements.\n\n **5.** You need to pay first so your Order will get received.\n\n**6.** Sharing the Product is forbidden; applies to License, HWID or IP bound products.\n\n**7.** You are not allowed to resell anything from my shop if you are not a reseller.\n\n**8.** For more information about a product ask <@921103030357725204>.\n\n**9.** Asking for some % Sale is forbidden.\n\n**10.** Warranty only applies to Products i have control over it; If you are a Loyal buyer or Booster the Warranty applies to the whole Shop.\n\n**11.** Warranty only activates after leaving a vouch/review in <#931782186233905273>\n\n**12.** The ToS can change at any time, if that occurs you automatically accept the changes.", color=0x4B0082)

            await webhook.send(embed=embedVar, username="Shop ToS")


def setup(client):
    filename = os.path.basename(__file__)[:-3]
    if validators.url(webhook_check(filename)):
        if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
            asyncio.set_event_loop_policy(
                asyncio.WindowsSelectorEventLoopPolicy())
        if asyncio.run(webhook_url_check(webhook_check(filename))) is True:
            client.add_cog(Tos(client))

            logging_switch(filename)
    else:
        logging.error(f"{filename.capitalize()} webhook not found!")
