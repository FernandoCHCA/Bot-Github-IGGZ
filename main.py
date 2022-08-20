import asyncio
import os
import datetime
import nextcord
from time import sleep
from nextcord.ext import commands
from nextcord import Interaction
#from dotenv import load_dotenv 

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True
bot = commands.Bot(command_prefix='-', intents=intents, help_command=None, case_insensitive=True)

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name="Visual Studio Code"))
    print('\n------------------------------------------------------------')
    print(f'          El bot {bot.user} esta en linea...')
    print('------------------------------------------------------------\n')

@bot.command()
async def camera(ctx:Interaction):
    await ctx.send('Logitech')

#Cogs
for fn in os.listdir('./cogs'):
    if fn.endswith('.py'):
        bot.load_extension(f"cogs.{fn[:-3]}")


if __name__ == '__main__':
    bot.run(os.environ["DISCORD_TOKEN"])