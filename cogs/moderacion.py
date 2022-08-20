import nextcord
from config import *
from nextcord import slash_command, Interaction
from nextcord.ext import commands

class Moderacion(commands.Cog):
    def __init__(self, client):
        self.client = client


    @slash_command(name='kick', description='Expulsa a un miembro', guild_ids=[ServersID])
    async def kick(
        self,
        ctx:Interaction,
        member: nextcord.Member = nextcord.SlashOption(
            name='member',
            description='Por favor, seleccione un miembro'
        ),
        reason: str = nextcord.SlashOption(
            name='reason',
            description='Por favor, indique la razón',
            required=False #This will make this option as a Optional.
        )
    ):
        if not reason: reason="Ninguna razón"
        await member.kick(reason=reason)
        await ctx.response.send_message(f"{member} ha sido expulsado por {ctx.user.mention} por {reason}")

    @slash_command(name='ban', description='Banea a un miembro', guild_ids=[ServersID])
    async def ban(
        self,
        ctx:Interaction,
        member: nextcord.Member = nextcord.SlashOption(name='member', description='Por favor, seleccione un miembro'),
        reason: str = nextcord.SlashOption(name='reason', description='Por favor, indique la razón', required=False)
    ):
        if not reason: reason = "Ninguna razón"
        await member.ban(reason=reason)
        await ctx.response.send_message(f"{member} ha sido baneado por {ctx.user.mention} por {reason}")

    @slash_command(name='unban', description='Unbanea a un miembro', guild_ids=[ServersID])
    async def unban(
        self,
        ctx:Interaction,
        member: nextcord.User = nextcord.SlashOption(name='member', description='Por favor, proporcione un ID de usuario')
    ): 
        await ctx.guild.unban(user=member)
        await ctx.response.send_message(f"{member} ha sido unbaneado por {ctx.user.mention}.")



def setup(client):
    client.add_cog(Moderacion(client))