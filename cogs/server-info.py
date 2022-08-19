from config import *
import nextcord
from nextcord.ext import commands
from nextcord import Embed, Interaction, slash_command, Member, SlashOption, ChannelType

class ServerInfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.slash_command(guild_ids=[ServersID], name='server-info', description='Mira la informacion del servidor!')
    async def server_info(self, interaction: Interaction):
        role_count = len(interaction.guild.roles)
        list_of_bots = [bot.mention for bot in interaction.guild.members if bot.bot]
        embed = nextcord.Embed(color=0x1FD3F3)
        Contador_humanos = [interaction.guild.humans.count]
        Contador_humanos_Count = len(interaction.guild.humans.count)
        Contador_bots = [interaction.guild.bots.count]
        Contador_bots_Count = len(interaction.guild.bots.count)
        embed.set_author(name=interaction.guild)
        embed.set_thumbnail(interaction.guild.icon)
        embed.add_field(name='Owner', value=interaction.guild.owner, inline=False)
        embed.add_field(name='Creado', value=interaction.guild.created_at.__format__('%d/%m/%Y, %H:%M:%S PM'), inline=False)
        embed.add_field(name='Contador de Miembros', value='{} humanos | {} bots | {} total'.format(Contador_humanos_Count, Contador_bots_Count, interaction.guild.member_count), inline=False)
        embed.add_field(name='Top rol', value=interaction.guild.roles[-31])
        embed.add_field(name='Bots', value=list_of_bots, inline=False)
        embed.set_footer(text=f'Requested by: {interaction.user.name}#{interaction.user.discriminator}\n{Fecha_actual}', icon_url='https://i.ibb.co/nCCJ2Wb/378-3782140-discord-server-icon-cute-imagenes-para-perfil-de.png')
        await interaction.response.send_message(embed=embed)

#Setup 
def setup(client):
    client.add_cog(ServerInfo(client))