import asyncio
import os
import datetime
import nextcord
from config import *
from time import sleep
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

class EmbedModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "Embed Maker",
        )

        self.emTitle = nextcord.ui.TextInput(label = "Embed Title", min_length = 2, max_length = 124, required = True, placeholder = "Introduzca el título del embed aquí!")
        self.add_item(self.emTitle)

        self.emDesc = nextcord.ui.TextInput(label = "Embed Description", min_length = 5, max_length = 4000, required = True, placeholder = "Introduzca la descripcion del embed aquí!", style = nextcord.TextInputStyle.paragraph)
        self.add_item(self.emDesc)

        self.emColor : str = nextcord.ui.TextInput(label = "Embed Color", min_length = 6, max_length = 6, required = False, placeholder = "Introduzca el color en hexadecimal del embed aquí!")
        self.add_item(self.emColor)

    async def callback(self, interaction: Interaction) -> None:
        title = self.emTitle.value
        description = self.emDesc.value
        colour = self.emColor.value
        if colour:
            embed.colour=int("0x" + colour, 16)
        embed = nextcord.Embed(title=title, description=description, colour=colour)
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