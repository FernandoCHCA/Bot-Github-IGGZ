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
        embed=nextcord.Embed(
            title='Usuario Kickeado!!',
            color=0xEC2424
            )
        embed.add_field(name='Kickeado por', value=ctx.user.mention, inline=False)
        embed.add_field(name='Miembro', value=member, inline=False)
        embed.add_field(name='Razón', value=reason, inline=False)
        embed.set_thumbnail(member.avatar)
        await ctx.response.send_message(embed=embed)
        #await ctx.response.send_message(f"{member} ha sido expulsado por {ctx.user.mention} por {reason}")

    @slash_command(name='ban', description='Banea a un miembro', guild_ids=[ServersID])
    async def ban(
        self,
        ctx:Interaction,
        member: nextcord.Member = nextcord.SlashOption(name='member', description='Por favor, seleccione un miembro'),
        reason: str = nextcord.SlashOption(name='reason', description='Por favor, indique la razón', required=False)
    ):
        if not reason: reason="Ninguna razón"
        if not duration: duration="Tiempo indefinido"
        await member.kick(reason=reason, duration=duration)
        embed=nextcord.Embed(
            title='Nuevo ban!',
            color=0xEC2424
            )
        embed.add_field(name='Kickeado por', value=ctx.user.mention, inline=False)
        embed.add_field(name='Miembro', value=member, inline=False)
        embed.add_field(name='Razón', value=reason, inline=False)
        embed.add_field(name='Duración', value=duration, inline=False)
        embed.set_thumbnail(member.avatar)
        await ctx.response.send_message(embed=embed)

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