import nextcord
from nextcord.ext import commands
from nextcord import Embed, Interaction, slash_command, Member, SlashOption, ChannelType
from config import *

class Embed_Modals_Cog(commands.Cog):
    def __init__(self, client):
        self.client = client

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
        return await interaction.response.send_message(embed=embed)


    @bot.slash_command(name="embed", description="Crea un Embed personalizado!", guild_ids=[ServersID])
    async def embed(interaction: Interaction):
        await interaction.response.send_modal(EmbedModal())

#Setup 
def setup(client):
    client.add_cog(Embed_Modals_Cog(client))