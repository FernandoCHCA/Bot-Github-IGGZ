from config import *
import nextcord
from nextcord.ext import commands
from nextcord import Embed, Interaction, slash_command, Member, SlashOption, ChannelType

class ServerInfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.slash_command(guild_ids=[ServersID], name='server-info', description='Mira la informacion del servidor!')
    async def server_info(self, ctx:Interaction):
        embed = nextcord.Embed(color=0x1FD3F3)
        Contador_humanos = len(ctx.guild.humans)
        Contador_bots = len(ctx.guild.bots)
        Contador_roles = len(ctx.guild.roles)
        Contador_emojis = len(ctx.guild.emojis)
        list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
        list_of_roles = []
        current_lenght = 0
        for role in ctx.guild.roles:

            if current_lenght + len(role.mention) + 2 <= 1012: # +2 is for ' ,' separator between roles; 1012 is 1023 - 11, 11 is length of the phrase 'and more...'
                list_of_roles.append(role.mention)
                current_lenght += len(role.mention) + 2 # length of the role mention + 2 for ' ,' separator between roles

            else:
                list_of_roles.append("and more...")
                break

        msg: str = None
        if msg:
            server, found = bot.find_server(msg)
        if not found:
            return await bot.send(server)
        else:
            server = ctx.message.server
        emojis = [str(x) for x in server.emojis]

        embed.set_author(name=ctx.guild)
        embed.set_thumbnail(ctx.guild.icon)
        embed.add_field(name='Owner', value=ctx.guild.owner.mention, inline=False)
        embed.add_field(name='Creado', value=ctx.guild.created_at.__format__('%d/%m/%Y, %H:%M:%S PM'), inline=False)
        embed.add_field(name='Contador de Miembros', value='**〔**🧒🏻​ {} humanos**〕** | **〔**🤖​ {} bots**〕** | **〔**🧔🏻​ {} total**〕**'.format(Contador_humanos, Contador_bots, ctx.guild.member_count), inline=False)
        embed.add_field(name=f'Bots〔{Contador_bots}〕', value=list_of_bots, inline=False)
        embed.add_field(name=f'Roles〔{Contador_roles}〕', value=", ".join(list_of_roles), inline=False)
        embed.add_field(name=f'Emojis〔{Contador_emojis}〕', value=", ".join(emojis), inline=False)
        await ctx.response.send_message(embed=embed)

#Setup 
def setup(client):
    client.add_cog(ServerInfo(client))