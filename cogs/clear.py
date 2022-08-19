from config import *
import nextcord
import asyncio
from nextcord.ext import commands
from nextcord import Embed, Interaction, slash_command, Member, SlashOption, ChannelType

class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.slash_command(guild_ids=[ServersID], name='clear', description='Borra la cantidad especifica de mensajes que gustes!')
    async def Clear(self, interaction: Interaction, amount:str):
        if amount == 'all':
            await interaction.channel.purge()
            embed=nextcord.Embed(description="**Se han borrado todos los mensajes**", color=0x1FD3F3)
            await interaction.response.send_message(embed=embed, ephemeral=True)
            await asyncio.sleep(20.0)
            await interaction.delete_original_message()
        else:
            await interaction.channel.purge(limit=(int(amount)))
            embed=nextcord.Embed(description=f"**Mensajes borrados**: {amount}", color=0x1FD3F3)
            await interaction.response.send_message(embed=embed, ephemeral=True)
            await asyncio.sleep(20.0)
            await interaction.delete_original_message()

#Setup 
def setup(client):
    client.add_cog(Clear(client))