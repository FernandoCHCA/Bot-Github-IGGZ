from config import *
import nextcord
from nextcord.ext import commands
from nextcord import Embed, Interaction, slash_command, Member, SlashOption, ChannelType

class ProfileServer(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.slash_command(guild_ids=[ServersID], name='profile-user', description="Mira el perfil de un usuario!")
    async def Profile(self, interaction: Interaction, user:nextcord.Member):
        embed=nextcord.Embed(title="Informacion del usuario", url='https://www.youtube.com/channel/UCxjRO--ufLCnThv15pIe1lQ', color=0x1FD3F3)
        embed.add_field(name='Usuario', value=user.mention, inline=False)
        embed.add_field(name='ID', value=user.id, inline=False)
        embed.add_field(name='Registrado', value=user.created_at.__format__('%d/%m/%Y, %H:%M:%S'), inline=False)
        embed.add_field(name='Se unio', value=user.joined_at.__format__('%d/%m/%Y, %H:%M:%S'), inline=False)
        embed.add_field(name='Rol mas alto', value=user.roles[-2], inline=False)
        embed.set_thumbnail(user.avatar)
        embed.set_footer(text=f'Requested by: {interaction.user.name}#{interaction.user.discriminator}\n{Fecha_actual}', icon_url='https://i.ibb.co/nCCJ2Wb/378-3782140-discord-server-icon-cute-imagenes-para-perfil-de.png')
        embed.set_image(url='https://i.ibb.co/XzNGGC4/Cartel-servidor.png')
        #Profile_embed.set_image(url='https://i.ibb.co/DzXLq1K/kgCYlv0.gif') # GIF DE LINEA DE COLORES
        await interaction.response.send_message(embed=embed)

#Setup 
def setup(client):
    client.add_cog(ProfileServer(client))