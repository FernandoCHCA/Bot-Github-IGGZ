from config import *
import requests
import nextcord
from nextcord.ext import commands
from nextcord import Embed, Interaction, slash_command, Member, SlashOption, ChannelType

class Hello(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.command()
    async def hello(self, interaction: Interaction):
        await interaction.response.send_message('Hola papu')
#Setup 
def setup(client):
    client.add_cog(Hello(client))