import nextcord
from nextcord.ext import commands
from nextcord import Embed, Interaction, slash_command, Member, SlashOption, ChannelType

ServersID = 994288503103959051

class Embed(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Embed command
    @slash_command(name='create-embed', description='Create embed.', guild_ids=[ServersID])
    async def embed_create(self, 
    ctx:Interaction,
    channel: nextcord.abc.GuildChannel = nextcord.SlashOption(channel_types=[ChannelType.text],name='channel', description='Please select a channel', required=False),
    author: str = nextcord.SlashOption(name='embed-author', description='Entre the author msg', required=False),
    author_icon: nextcord.Attachment = nextcord.SlashOption(name='embed-author-icon', description='Please select a image file', required=False),
    title: str = nextcord.SlashOption(name='embed-title', description='Entre title msg.', required=False),
    description: str = nextcord.SlashOption(name='embed-description', description='Entre description msg.', required=False),
    footer: str = nextcord.SlashOption(name='embed-footer', description='Entre footer msg.', required=False),
    footer_icon: nextcord.Attachment = nextcord.SlashOption(name='embed-footer-icon', description='Please select a image file for footer icon', required=False),
    image: nextcord.Attachment = nextcord.SlashOption(name='embed-image', description='Please select a image file for embed image', required=False),
    thumbnail: nextcord.Attachment = nextcord.SlashOption(name='embed-thumbnail', description='Please select a image file for embed thumbnail', required=False),
    colour: str = nextcord.SlashOption(name='embed-colour', description='Please provide a hex code', required=False)
    ):
        embed = nextcord.Embed()
        if not channel:
            channel = ctx.channel
            
        if author is not None and author_icon is not None:
            embed.set_author(name=author, icon_url=author_icon)
        elif author is not None and author_icon is None:
            embed.set_author(name=author)
        elif author is None and author_icon is not None:
            pass
        if title:
            embed.title=title
        if description:
            embed.description=description
        if footer_icon is not None and footer_icon is not None:
            embed.set_footer(text=footer, icon_url=footer_icon)
        elif footer is not None and footer_icon is None:
            embed.set_footer(text=footer)
        elif footer is None and footer_icon is not None:
            pass
        if image:
            embed.set_image(url=image)
        if thumbnail:
            embed.set_thumbnail(url=thumbnail)
        if colour:
            embed.colour=int("0x" + colour, 16)
        if not author and not title and not description and not footer and not image and not thumbnail and not colour:
            await ctx.response.send_message("Please write any of these values", ephemeral=True)
        else:
            await channel.send(embed=embed)
            await ctx.response.send_message(f"Embed sent to {channel}")

#Setup 
def setup(client):
    client.add_cog(Embed(client))