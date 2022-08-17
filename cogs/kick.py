import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions

class kick(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Kick command
    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self,ctx,member: nextcord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.reply(f"Kicked {member}\nReason:{reason}")
        await member.send(f"You Got Kick From The Server \nReason:{reason}")

    #Exeption in case if the member doen't have the permissions
    @kick.error
    async def kick_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.reply("You Don't Have The Permissions To Kick !")

    #Kick Command Exception
    @kick.error
    async def kick_error(self,ctx , error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"<@{ctx.author.id}> \nThis Command Usage Is ` -kick [member] [reason] `")

#Setup 
def setup(client):
    client.add_cog(kick(client))