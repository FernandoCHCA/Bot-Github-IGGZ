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
bot = commands.Bot(command_prefix='=', intents=intents, help_command=None, case_insensitive=True)

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name="Visual Studio Code"))
    print('\n------------------------------------------------------------')
    print(f'          El bot {bot.user} esta en linea...')
    print('------------------------------------------------------------\n')

class Pet(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "Your pet",
            timeout=5 * 60,  # 5 minutes
        )

        self.name = nextcord.ui.TextInput(
            label="Your pet's name",
            min_length=2,
            max_length=50,
        )
        self.add_item(self.name)

        self.description = nextcord.ui.TextInput(
            label="Description",
            style=nextcord.TextInputStyle.paragraph,
            placeholder="Information that can help us recognise your pet",
            required=False,
            max_length=1800,
        )
        self.add_item(self.description)

        self.pet_type = nextcord.ui.Select(
            options=[
                nextcord.SelectOption(label="Dog", emoji="🐶"),
                nextcord.SelectOption(label="Cat", emoji="🐱"),
                nextcord.SelectOption(label="Bird", emoji="🐦"),
                nextcord.SelectOption(label="Fish", emoji="🐟"),
                nextcord.SelectOption(label="Other", emoji="🐰"),
            ],
            min_values=1,
            max_values=1,
            placeholder="Type of pet",
        )
        self.add_item(self.pet_type)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        response = f"{interaction.user.mention}'s favourite pet's name is {self.name.value}."
        response += f"\nThe type of pet is {self.pet_type.values[0]}."
        if self.description.value != "":
            response += (
                f"\nTheir pet can be recognized by this information:\n{self.description.value}"
            )
        await interaction.send(response)

@bot.slash_command(
    name="pet",
    description="Describe your favourite pet",
    guild_ids=[ServersID]
)
async def send(interaction: nextcord.Interaction):
    modal = Pet()
    await interaction.response.send_modal(modal)

#Cogs
for fn in os.listdir('./cogs'):
    if fn.endswith('.py'):
        bot.load_extension(f"cogs.{fn[:-3]}")


if __name__ == '__main__':
    bot.run(os.environ["DISCORD_TOKEN"])