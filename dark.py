import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random

token = 'NjAzMzkxNjQ4MzYxMjE4MDkz.XYl2QQ.X43pA1JUCZoI-5rRq8n52WX20GM'
client = commands.Bot(command_prefix = '.')

class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return '*{2}* es гомосексуальный'.format(ctx, to_slap, argument)

class Selacome(commands.Converter):
    async def convert(self, ctx, argument):
        sela_come = random.choice(ctx.guild.members)
        return 'selacome *{2}*'.format(ctx, sela_come, argument)


@client.command()
async def Cyk(ctx, *, reason: Slapper):
    await ctx.send(reason)

@client.command()
async def selacome(ctx, *, reason: Selacome):
    await ctx.send(reason)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('con tus sentimientos.'))
    print('Bot is ready.')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def hello(ctx):
    embed = discord.Embed(
        title = 'Dark Phoenix',
        description = 'Bienvenidos a Dark Phoenix SF!',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='Dark Phoenix SF v1.3 © 2019-2019 CarlosA1200#0117')
    embed.set_image(url='https://cdn.discordapp.com/attachments/609533658046398474/626550411767316502/gato.jpg')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/609533658046398474/626550411767316502/gato.jpg')
    embed.set_author(name='...',
    icon_url='https://cdn.discordapp.com/attachments/609533658046398474/626550411767316502/gato.jpg')
    embed.add_field(name='Ayuda', value='Para ayuda utiliza .aiuda', inline=False)
    embed.add_field(name='Comandos', value='Para una lista de comandos utiliza .comandos', inline=True)

    await ctx.send(embed=embed)

@client.command()
async def rule9(ctx):
    embed = discord.Embed(
        title = 'Lo Pendejo Se paga Aparte',
        colour = discord.Colour.red()
    )
    await ctx.send(embed=embed)

@client.command()
async def medasadmin(ctx):
    await ctx.send('"No"-sfloy ')

@client.command()
async def comandos(ctx):
    await ctx.send('.nepe, .ping, .Mantecas, .hello, .add, .pp, .selacome, .slap')

@client.command()
async def stfu(ctx):
    await ctx.send('Shut the fuck up')

@client.command()
async def conquejuegas(ctx):
    await ctx.send('con tus sentimientos')

@client.command()
async def ayuda(ctx):
    await ctx.send('buscate tu propia ayuda.')

@client.command()
async def nepe(ctx):
    await ctx.send('Cual? el que no tienes?')

@client.command()
async def alex(ctx):
    await ctx.send('Es muy guapo y hermoso jajaja xd')

@client.command()
async def pp(ctx):
    embed = discord.Embed(
        title = 'PP',
        description = '8=========D!',
        colour = discord.Colour.blue()
    )

    await ctx.send(embed=embed)

@client.command()
async def dicionario(ctx):
    embed = discord.Embed(
        title = 'Dark Phoenix',
        description = 'Para los mecos que no saben ruso!',
        colour = discord.Colour.blue()
    )

    embed.add_field(name='Palabras', value='Cyk: Perra, гомосексуальный: homosexual', inline=True)

    await ctx.send(embed=embed)

@client.command()
async def wawis(ctx):
    await ctx.send('QUE VERGA ES ESO?')

@client.command()
async def ping(ctx):
    await ctx.send(f':ping_pong:Pong! {client.latency} ')

@client.command()
async def Mantecas(ctx):
     await ctx.send('<@474024870078840833>, la manteca se ardio y se derritio. XD')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@client.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)



client.run(token)
