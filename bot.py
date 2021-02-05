import discord
import os
from discord.ext import commands, tasks
from time import sleep

client = commands.Bot(command_prefix = '$')
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot started.')
    await client.change_presence(activity=discord.Game('Wish Shopping | $buy <username> <x> <y> <z> <amount> <item>'))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.purge(limit=100)
        await ctx.send('Please pass in all required arguments. Most likely you are using $buy. The proper syntax for it is $buy <username> <x> <y> <z> <amount> <item>.')
        sleep(10)
        await ctx.channel.purge(limit=100)
    if isinstance(error, commands.CommandNotFound):
        await ctx.channel.purge(limit=100)
        await ctx.send('Unknown command. Use .help for a list of commands')
        sleep(10)
        await ctx.channel.purge(limit=100)
    if isinstance(error, commands.MissingPermissions):
        await ctx.channel.purge(limit=100)
        await ctx.send('You do not have the required permissions to run this command.')
        sleep(10)
        await ctx.channel.purge(limit=100)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {client.latency * 1000}ms')

def owner(ctx):
    return ctx.author.id == 317394276189208576 or 430471933247750147

@client.command()
@commands.check(owner)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.check(owner)
async def status(ctx, *, txt):
    await client.change_presence(activity=discord.Game(txt))

@client.command()
async def buy(ctx, username, x, y, z, amount, *, item):
    await ctx.channel.purge(limit=100)
    await ctx.send('Thank you for shopping at Wish! Please make sure your DMs are open so we can confirm your order and ask for additional info if needed.')
    channel = client.get_channel(806986686612766740)
    await channel.send(f'{username} requested {amount} of {item}. The location they provided is {x}, {y}, {z}. Their Discord is {ctx.author.mention}. <@&806997905406820362>')
    sleep(10)
    await ctx.channel.purge(limit=100)

@client.command()
async def buymulti(ctx, username, x, y, z, *, info):
    await ctx.channel.purge(limit=100)
    await ctx.send('Thank you for shopping at Wish! It may take longer to get your order due to ordering more than one item. Please make sure your DMs are open so we can confirm your order and ask for additional info if needed.')
    channel = client.get_channel(807051693522419733)
    await channel.send(f'{username} requested multiple items. The location they provided is {x}, {y}, {z}. Their Discord is {ctx.author.mention}. Here is the list of items they provided: {info} <@&806997905406820362>')
    sleep(10)
    await ctx.channel.purge(limit=100)

@client.command()
async def contact(ctx, *, msg):
    await ctx.channel.purge(limit=100)
    await ctx.send('Thank you for contacting Wish! You will most likely get a DM from someone regarding your request.')
    channel = client.get_channel(807045544559378463)
    await channel.send(f'{ctx.author.mention}: {msg}')
    sleep(10)
    await ctx.channel.purge(limit=100)

@client.command()
async def report(ctx, member : discord.Member, *, reason):
    await ctx.channel.purge(limit=100)
    await ctx.send('Thanks for reporting them! We will see the report soon. They will not see who reported them, only staff will. Reports of high staff will not be considered.')
    channel = client.get_channel(807045460803846194)
    await channel.send(f'{ctx.author.mention} reported {member.mention} for {reason}.')
    sleep(10)
    await ctx.channel.purge(limit=100)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODA2OTgxNTc2OTEwMzA3MzI4.YBxWKA.A47Vq8jsWPlmSHCYOseeJasoWfk')
