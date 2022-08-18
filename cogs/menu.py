from config import *
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class Dropdown(nextcord.ui.Select):
    def __init__(self):

        options = [
            nextcord.SelectOption(
                label="Red", description="Este color es para puro Power Ranger", emoji="🟥"
            ),
            nextcord.SelectOption(
                label="Green", description="Este color es para puro ChampionShip", emoji="🟩"
            ),
            nextcord.SelectOption(
                label="Blue", description="Este color es para puro Sayayin", emoji="🟦"
            ),
        ]

        super().__init__(
            placeholder="Escoge tu color favorito...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f"Tu color favorito es {self.values[0]}")

class DropdownView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())

class Menu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.slash_command()
    async def colour(interaction: Interaction):
        view = DropdownView()
        await interaction.send("Veamos que team color eres:", view=view)

#Setup 
def setup(client):
    client.add_cog(Menu(client))