import nextcord
from config import *
from nextcord import slash_command, Interaction
from nextcord.ext import commands

class Modals(commands.Cog):
    def __init__(self, client):
        self.client = client

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


def setup(client):
    client.add_cog(Modals(client))