import nextcord
from config import *
from nextcord import slash_command, Interaction
from nextcord.ext import commands

class Mensaje(commands.Cog):
    def __init__(self, client):
        self.client = client


    @bot.command(pass_context=True)
    async def dm(ctx:Interaction):
        user=await bot.get_user_info("User's ID here")
        await bot.send_message(user, "Your message goes here")
        # This works ^


def setup(client):
    client.add_cog(Mensaje(client))