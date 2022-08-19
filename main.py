import asyncio
import os
import datetime
import nextcord
from time import sleep
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, Member, Embed, ChannelType
from nextcord.ext.commands import has_permissions, MissingPermissions
#from dotenv import load_dotenv 

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')

intents = nextcord.Intents.default()
intents.members = True
#intents.message_content = True
bot = commands.Bot(command_prefix='-', intents=intents, help_command=None, case_insensitive=True)

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name="Visual Studio Code"))
    print('\n------------------------------------------------------------')
    print(f'          El bot {bot.user} is online...')
    print('------------------------------------------------------------\n')

#Cogs
for fn in os.listdir('./cogs'):
    if fn.endswith('.py'):
        bot.load_extension(f"cogs.{fn[:-3]}")

# def current_date_format(date):
#     months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
#     day = date.day
#     month = months[date.month - 1]
#     year = date.year
#     hour = date.hour
#     minute = date.minute
#     second = date.second
#     messsage = "{} {}, {}, {}:{}:{}".format(month, day, year, hour, minute, second)

#     return messsage

# ServersID = 994288503103959051
# Fecha_actual = current_date_format(datetime.datetime.now())
# #Fecha_procesada = Fecha_actual.__format__('%d/%m/%Y, %H:%M:%S')

# @bot.slash_command(guild_ids=[ServersID], name='ip-server', description="Mira la ip del servidor!")
# async def Ip_servidor(interaction: Interaction):
#     embed=nextcord.Embed(title="IP:", description="Servidor en proceso...", color=0x1FD3F3)
#     await interaction.response.send_message(embed=embed)

# @bot.slash_command(guild_ids=[ServersID], name='profile-user', description="Mira el perfil de un usuario!")
# async def Profile(interaction: Interaction, user:nextcord.Member):
#     embed=nextcord.Embed(title="Informacion del usuario", url='https://www.youtube.com/channel/UCxjRO--ufLCnThv15pIe1lQ', color=0x1FD3F3)
#     embed.add_field(name='Usuario', value=user.mention, inline=False)
#     embed.add_field(name='ID', value=user.id, inline=False)
#     embed.add_field(name='Registrado', value=user.created_at.__format__('%d/%m/%Y, %H:%M:%S'), inline=False)
#     embed.add_field(name='Se unio', value=user.joined_at.__format__('%d/%m/%Y, %H:%M:%S'), inline=False)
#     embed.add_field(name='Categoria de rol mas alto', value=user.top_role, inline=False)
#     embed.set_thumbnail(user.avatar)
#     embed.set_footer(text=f'Solicitado por: {interaction.user.name}#{interaction.user.discriminator}\nFecha: {Fecha_actual}')
#     embed.set_image(url='https://i.ibb.co/XzNGGC4/Cartel-servidor.png')
#     #Profile_embed.set_image(url='https://i.ibb.co/DzXLq1K/kgCYlv0.gif') # GIF DE LINEA DE COLORES
#     await interaction.response.send_message(embed=embed)

# @bot.slash_command(guild_ids=[ServersID], name='server-info', description='Mira la informacion del servidor!')
# async def server_info(interaction: Interaction):
#     role_count = len(interaction.guild.roles)
#     list_of_bots = [bot.mention for bot in interaction.guild.members if bot.bot]
#     embed = nextcord.Embed(color=0x1FD3F3)
#     embed.set_author(name=interaction.guild)
#     embed.set_thumbnail(interaction.guild.icon)
#     embed.add_field(name='Servidor configurado por', value=interaction.guild.owner, inline=False)
#     embed.add_field(name='ID del propietario', value=interaction.guild.owner_id, inline=False)
#     embed.add_field(name='Nivel de verificacion', value=interaction.guild.verification_level, inline=False)
#     embed.add_field(name='Miembros', value=interaction.guild.member_count, inline=False)
#     embed.add_field(name='Top rol', value=interaction.guild.roles[-31])
#     embed.add_field(name='Servidor creado', value=interaction.guild.created_at.__format__('%d/%m/%Y, %H:%M:%S'), inline=False)
#     embed.add_field(name='Bots', value=list_of_bots, inline=False)
#     embed.set_footer(text=f'Solicitado por: {interaction.user.name}#{interaction.user.discriminator}\nFecha: {Fecha_actual}')
#     await interaction.response.send_message(embed=embed)

# @bot.slash_command(guild_ids=[ServersID], name='clear', description='Borra la cantidad especifica de mensajes que gustes!')
# async def Clear(interaction: Interaction, amount:str):
#     if amount == 'all':
#         await interaction.channel.purge()
#         embed=nextcord.Embed(title="Se han borrado todos los mensajes", color=0x1FD3F3)
#         embed.set_footer(text='Este mensaje desaparecerá en 20 segundos')
#         await interaction.response.send_message(embed=embed, ephemeral=True)
#         await asyncio.sleep(20.0)
#         await interaction.delete_original_message()
#     else:
#         await interaction.channel.purge(limit=(int(amount)))
#         embed=nextcord.Embed(title=f"Mensajes borrados: {amount}", color=0x1FD3F3)
#         embed.set_footer(text='Este mensaje desaparecerá en 20 segundos')
#         await interaction.response.send_message(embed=embed, ephemeral=True)
#         await asyncio.sleep(20.0)
#         await interaction.delete_original_message()

# # Menu
# class Dropdown(nextcord.ui.Select):
#     def __init__(self):

#         options = [
#             nextcord.SelectOption(
#                 label="Red", description="Este color es para puro Power Ranger", emoji="🟥"
#             ),
#             nextcord.SelectOption(
#                 label="Green", description="Este color es para puro ChampionShip", emoji="🟩"
#             ),
#             nextcord.SelectOption(
#                 label="Blue", description="Este color es para puro Sayayin", emoji="🟦"
#             ),
#         ]

#         super().__init__(
#             placeholder="Escoge tu color favorito...",
#             min_values=1,
#             max_values=1,
#             options=options,
#         )

#     async def callback(self, interaction: nextcord.Interaction):
#         await interaction.response.send_message(f"Tu color favorito es {self.values[0]}")

# class DropdownView(nextcord.ui.View):
#     def __init__(self):
#         super().__init__()
#         self.add_item(Dropdown())

# @bot.slash_command()
# async def colour(interaction: Interaction):
#     view = DropdownView()
#     await interaction.send("Veamos que team color eres:", view=view)

#bot.run('DISCORD_TOKEN')
if __name__ == '__main__':
    bot.run(os.environ["DISCORD_TOKEN"])