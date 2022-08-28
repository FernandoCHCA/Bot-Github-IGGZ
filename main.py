import asyncio
import os
import nextcord
# import aiosqlite
import sys
import sqlite3
from sqlite3 import Error
from config import *
from nextcord.ext import commands
from nextcord import Interaction, Intents
#from dotenv import load_dotenv 

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None, case_insensitive=True)

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name="Visual Studio Code"))
    print('\n------------------------------------------------------------')
    print(f'          El bot {bot.user} esta en linea...')
    print('------------------------------------------------------------\n')
    try:
        async with sqlite3.connect("main.db") as db: #1 Establezco conexion
            async with db.cursor() as cursor:
                await cursor.execute("CREATE TABLE IF NOT EXISTS IF NOT EXISTS users (id INTEGER, guild INTEGER")
                print("Tabla creada exitosamente")
            await db.commit()
    except Error as e:
        print(e)
    except Exception:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        if db:
            db.close()

@bot.command()
async def adduser(ctx:Interaction, member:nextcord.Member):
    try:
        async with sqlite3.connect("main.db") as db:
            async with db.cursor() as cursor:
                await cursor.execute("SELECT id FROM users WHERE guild = ?", (ctx.guild.id))
                data = await db.fetchone()
                if data:
                    await cursor.execute('UPDATE users SET id = ? WHERE guild = ?', (member.id,ctx.guild.id))
                else:
                    await cursor.execute('INSERT INTO users (id, guild) VALUES (?, ?)', (member.id,ctx.guild.id))
            await db.commit()
    except Error as e:
        print(e)
    except Exception:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        if db:
            db.close()

class EmbedModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "Embed Maker",
        )

        self.emTitle = nextcord.ui.TextInput(label = "Embed Title", min_length = 2, max_length = 124, required = True, placeholder = "Introduzca el título del embed aquí!")
        self.add_item(self.emTitle)

        self.emDesc = nextcord.ui.TextInput(label = "Embed Description", min_length = 5, max_length = 4000, required = True, placeholder = "Introduzca la descripcion del embed aquí!", style = nextcord.TextInputStyle.paragraph)
        self.add_item(self.emDesc)

        self.emColor : int = nextcord.ui.TextInput(label = "Embed Color", min_length = 6, max_length = 6, required = False, placeholder = "Introduzca el color en hexadecimal del embed aquí!")
        self.add_item(self.emColor)

    async def callback(self, interaction: Interaction) -> None:
        title = self.emTitle.value
        description = self.emDesc.value
        colour = int('0x' + self.emColor.value, 16)
        embed = nextcord.Embed(title=title, description=description, colour=colour)
        # embed = nextcord.Embed(title=title, description=description, colour=nextcord.Color.random())
        return await interaction.response.send_message(embed=embed)

@bot.slash_command(name="embed", description="Crea un Embed personalizado!", guild_ids=[ServersID])
async def embed(interaction: Interaction):
    await interaction.response.send_modal(EmbedModal())

#Cogs
for fn in os.listdir('./cogs'):
    if fn.endswith('.py'):
        bot.load_extension(f"cogs.{fn[:-3]}")

if __name__ == '__main__':
    bot.run(os.environ["DISCORD_TOKEN"])