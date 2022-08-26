from config import *
import nextcord
from nextcord.ext import commands
from nextcord import Embed, Interaction, slash_command, Member, SlashOption

class comandos(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.event
    async def on_message(self, interaction: Interaction, message):
        if interaction.message.author == bot.user:
            return
        if interaction.message.content.startswith("!hola"):
            await interaction.response.send_message("Hola papu!")

    @bot.command()
    async def camara(interaction: Interaction):
        await interaction.send('Logitech')

#Setup 
def setup(client):
    client.add_cog(comandos(client))