import discord
from discord.ext import commands

import datetime
import pytz

from threading import Thread
from flask import Flask

import requests
from bs4 import BeautifulSoup

bot = commands.Bot(command_prefix='b!')

bot.remove_command('help')

time = datetime.datetime.utcnow()

# on intialization event
@bot.event
async def on_ready():

    # prints the initialization message on the right-hand side (console)
    print(
        f'================================================================================= \nDiscord Bot Name: {bot.user.name} \nHosting Platform: Dell Inspiron 5559 \nBot Developers: vprak#2265 \n================================================================================= \n\nBOT CONSOLE LOG BELOW: \n'
    )

    # changes the "Playing..." status of the bot
    await bot.change_presence(
        activity=discord.Game(name='some Bangers | b!help'))


# help command
@bot.command()
async def help(ctx):
    member = bot.get_user(ctx.author.id)

    embed = discord.Embed(title="**Help Section**", color=0x43E194, timestamp=time)

    embed.set_author(name='Bopz', icon_url='https://i.imgur.com/3sPd3Mj.png')

    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=f'{member.avatar_url}')

    embed.add_field(name=':newspaper: Help', value='`b!help` \n')

    embed.add_field(name=':musical_note: Music', value='`b!play <song>` \n', inline=False)

    embed.add_field(name=':man_pouting: Billboard', value='`b!bb` \n `b!billboard` \n', inline=False)

    embed.add_field(name=':information_source: Bot Info', value='`b!botinfo`', inline=False)

    await ctx.send(embed=embed)

    print('HELP Command Called')

@bot.command(aliases=['billbd', 'billboard','bboard'])
async def bb(ctx):
    url='https://www.billboard.com/charts/hot-100'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_='chart-list container')

    song_names = results.find_all('span', class_="chart-element__information__song text--truncate color--primary")
    songs = []
    for i in range(0, 10):
        songs.append(song_names[i].text.strip())

    artist_names = results.find_all('span', class_="chart-element__information__artist text--truncate color--secondary")
    artists = []
    for i in range(0, 10):
        artists.append(artist_names[i].text.strip())
        
    member = bot.get_user(ctx.author.id)

    embed = discord.Embed(title='**Billboard Top 10**', color=0x43E194, timestamp=time)

    embed.set_author(name='Bopz', icon_url='https://i.imgur.com/3sPd3Mj.png')

    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=f'{member.avatar_url}')

    for i in range(0,10):
        embed.add_field(name=f'{i+1}. {songs[i]}', value=f'by {artists[i]}', inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def play(ctx, song):
    member = bot.get_user(ctx.author.id)

    embed = discord.Embed(title='**Song Player**', color=0x43E194, timestamp=time)

    embed.set_author(name='Bopz', icon_url='https://i.imgur.com/3sPd3Mj.png')
    
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=f'{member.avatar_url}')

    embed.add_field(name='Playing', value='Song `currently under development`')

    await ctx.send(embed=embed)


@bot.command()
async def botinfo(ctx):
    member = bot.get_user(ctx.author.id)

    embed = discord.Embed(title='**Bot Info**', color=0x43E194, timestamp=time)

    embed.set_author(name='Bopz', icon_url='https://i.imgur.com/3sPd3Mj.png')
    
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=f'{member.avatar_url}')

    embed.add_field(name='**Developer**', value='<@533153734373539840>', inline=False)

    embed.add_field(name='Platform', value='[Dell Inspiron 5559](https://www.dell.com/support/home/en-us/product-support/product/inspiron-15-5559-laptop/docs)', inline=False)

    embed.add_field(name='Github Repository', value='[Bot Page](htstps://github.com/Vrushank17/Bopz)', inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    member = bot.get_user(ctx.author.id)

    embed = discord.Embed(title='**Ping**', color=0x43E194, timestamp=time)

    embed.set_author(name='Bopz', icon_url='https://i.imgur.com/3sPd3Mj.png')
    
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=f'{member.avatar_url}')

    embed.add_field(name=':ping_pong: Pong!', value=f'The latency is {round(bot.latency * 1000)} MS')

    await ctx.send(embed=embed)

    print('PING Command Called')

f = open('bot_token.txt')
token = f.readline()
bot.run(token)
