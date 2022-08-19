from config import *
import nextcord
from nextcord.ext import commands
from nextcord import Embed, Interaction, slash_command, Member, SlashOption, ChannelType

class Hello(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.command()
    async def hello(self, ctx):
        await ctx.send('Hola papu')
#Setup 
def setup(client):
    client.add_cog(Hello(client))