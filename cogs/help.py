import discord
from discord.ext import commands

class shop(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Help command loaded')

    @commands.command()
    async def help(self, ctx):

        helpembed = discord.Embed(
            colour = discord.Colour.blue(),
            title = 'Wish Shopping Commands',
            description = '$help | Shows this menu.\n$buy <username> <x> <y> <z> <amount> <item> | Buys an item.\n$buymulti\n$contact <message> | Contacts a staff member.\n$report <@mention> <reason> | Reports a player.'
        )
        helpembed.set_footer(text='Wish Shopping | DemocracyCraft')
        await ctx.send(embed=helpembed)

def setup(client):
    client.add_cog(shop(client))