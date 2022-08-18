from config import *
import nextcord
from nextcord.ext import commands
from nextcord import Embed, Interaction, slash_command, Member, SlashOption, ChannelType

class ProfileServer(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.slash_command(guild_ids=[ServersID], name='profile-user', description="Mira el perfil de un usuario!")
    async def Profile(interaction: Interaction, user:nextcord.Member):
        embed=nextcord.Embed(title="Informacion del usuario", url='https://www.youtube.com/channel/UCxjRO--ufLCnThv15pIe1lQ', color=0x1FD3F3)
        embed.add_field(name='Usuario', value=user.mention, inline=False)
        embed.add_field(name='ID', value=user.id, inline=False)
        embed.add_field(name='Registrado', value=user.created_at.__format__('%d/%m/%Y, %H:%M:%S'), inline=False)
        embed.add_field(name='Se unio', value=user.joined_at.__format__('%d/%m/%Y, %H:%M:%S'), inline=False)
        embed.add_field(name='Categoria de rol mas alto', value=user.top_role, inline=False)
        embed.set_thumbnail(user.avatar)
        embed.set_footer(text=f'Solicitado por: {interaction.user.name}#{interaction.user.discriminator}\nFecha: {Fecha_actual}')
        embed.set_image(url='https://i.ibb.co/XzNGGC4/Cartel-servidor.png')
        #Profile_embed.set_image(url='https://i.ibb.co/DzXLq1K/kgCYlv0.gif') # GIF DE LINEA DE COLORES
        await interaction.response.send_message(embed=embed)

#Setup 
def setup(client):
    client.add_cog(ProfileServer(client))