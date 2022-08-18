from config import *
import nextcord
from nextcord.ext import commands
from nextcord import Embed, Interaction, slash_command, Member, SlashOption, ChannelType

class ServerInfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.slash_command(guild_ids=[ServersID], name='server-info', description='Mira la informacion del servidor!')
    async def server_info(interaction: Interaction):
        role_count = len(interaction.guild.roles)
        list_of_bots = [bot.mention for bot in interaction.guild.members if bot.bot]
        embed = nextcord.Embed(color=0x1FD3F3)
        embed.set_author(name=interaction.guild)
        embed.set_thumbnail(interaction.guild.icon)
        embed.add_field(name='Servidor configurado por', value=interaction.guild.owner, inline=False)
        embed.add_field(name='ID del propietario', value=interaction.guild.owner_id, inline=False)
        embed.add_field(name='Nivel de verificacion', value=interaction.guild.verification_level, inline=False)
        embed.add_field(name='Miembros', value=interaction.guild.member_count, inline=False)
        embed.add_field(name='Top rol', value=interaction.guild.roles[-31])
        embed.add_field(name='Servidor creado', value=interaction.guild.created_at.__format__('%d/%m/%Y, %H:%M:%S'), inline=False)
        embed.add_field(name='Bots', value=list_of_bots, inline=False)
        embed.set_footer(text=f'Solicitado por: {interaction.user.name}#{interaction.user.discriminator}\nFecha: {Fecha_actual}')
        await interaction.response.send_message(embed=embed)

#Setup 
def setup(client):
    client.add_cog(ServerInfo(client))