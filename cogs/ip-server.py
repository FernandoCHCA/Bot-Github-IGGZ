from config import *
import nextcord
from nextcord.ext import commands
from nextcord import Embed, Interaction, slash_command, Member, SlashOption, ChannelType

class IpServer(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.slash_command(guild_ids=[ServersID], name='ip-server', description="Mira la ip del servidor!")
    async def Ip_servidor(self, interaction: Interaction):
        embed=nextcord.Embed(title="IP:", description="Servidor en proceso...", color=0x1FD3F3)
        await interaction.response.send_message(embed=embed)

#Setup 
def setup(client):
    client.add_cog(IpServer(client))