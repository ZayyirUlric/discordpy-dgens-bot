import csv
import asyncio
import discord
import time
from threading import Timer
from discord.ext import commands

bot = commands.Bot(command_prefix='<PREFIX>')

sass = True
talkback = False

@bot.event
async def on_ready():
    print('yes')

@bot.event
async def on_guild_join(guild):
    guild_talkback = {}
    guild_talkback[guild.id] = False
    with open('<PATH_TO_DIR>/guilds.csv', 'a') as f:
        for key in guild_talkback.keys():
            f.write("%s,%s\n"%(key,guild_talkback[key]))


@bot.command()
async def print(ctx, arg):
    await ctx.send(embed=discord.Embed(title=arg))

@bot.command()
async def remindme(ctx, arg):
    await ctx.send("gegegege ma'amser")
    rm_input = arg.split('/')
    rm_input_hour = rm_input[0]
    rm_input_str = rm_input[1]
    rm_tminus = float(rm_input_hour)*3600  
    await asyncio.sleep(rm_tminus)
    await ctx.send("{}, {}".format(ctx.message.author.mention, rm_input_str))

@bot.command()
async def switch(ctx, arg):
    with open('<PATH_TO_DIR>/guilds.csv') as f:
        guild_talkback = dict(filter(None, csv.reader(f)))
    print(guild_talkback)
    id = ctx.message.guild.id
    tb = guild_talkback[str(id)]
    if arg == 'on' and tb == "False":
        guild_talkback[str(id)] = True
        with open('<PATH_TO_DIR>/guilds.csv', 'w') as f:
            for key in guild_talkback.keys():
                f.write("%s,%s\n"%(key,guild_talkback[key]))
        await ctx.send(embed=discord.Embed(title="**[WARNING] MAMA MO MODE: ON**"))
    elif arg == 'off' and tb == "True":
        guild_talkback[str(id)] = False
        with open('<PATH_TO_DIR>/guilds.csv', 'w') as f:
            for key in guild_talkback.keys():
                f.write("%s,%s\n"%(key,guild_talkback[key]))
        await ctx.send(embed=discord.Embed(title='**[WARNING] MAMA MO MODE: OFF**'))
    else:
        await ctx.send('Invalid argument or redundant action.')

@bot.event
async def on_message(message):
    ctx = await bot.get_context(message)
    if message.author == bot.user:
        return
    if message.content.startswith('MM'):
        await bot.invoke(ctx)
    with open('<PATH_TO_DIR>/guilds.csv') as csv_file:
        reader = csv.reader(csv_file)
        guild_talkback = dict(reader)
    id = ctx.message.guild.id
    tb = guild_talkback[str(id)]
    if tb == "True":
        await message.channel.send('mama mo '+message.content)

TOKEN = '<TOKEN>'
bot.run(TOKEN)
