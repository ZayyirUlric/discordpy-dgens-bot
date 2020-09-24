# coding=utf8
import csv
import asyncio
import discord
import time
import random
from threading import Timer
from discord.ext import commands

################################################################################################
#                                 DEFINE VARIABLES HERE                                        #
PREFIX = ""
PATH_TO_DIR = "" # This is used for pointing to guild.csv
TOKEN = ''
#                                                                                              #
################################################################################################

bot = commands.Bot(command_prefix=PREFIX, help_command=None)
sass = True
talkback = False

@bot.event
async def on_ready():
    activity = discord.Activity(name='your mama mo', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)    

@bot.event
async def on_guild_join(guild):
    guild_talkback = {}
    guild_talkback[guild.id] = False
    with open(PATH_TO_DIR, 'a') as f:
        for key in guild_talkback.keys():
            f.write("%s,%s\n"%(key,guild_talkback[key]))

@bot.command()
async def help(ctx):
    help_info = '''
```
| Feature    | Arguments                  | Description                                     |
|------------|----------------------------|-------------------------------------------------|
| remindme   | <Hours> <Text>             | Reminds the user with a ping after X hours.     |
| switch     | on | off                   | Switches `Mama mo mode` on or off.              |
| print      | <text>                     | Prints text into an embed title.                |
| ha         | on mention of "ha"         | Prints "hatdog" upon mention of "ha".           |
| impostor   | on mention of "impostor"   | Prints if the user mentioned is an impostor.    |
```
'''
    await ctx.send(help_info)

@bot.command()
async def print(ctx, arg):
    await ctx.send(embed=discord.Embed(title=arg))

@bot.command()
async def remindme(ctx, *, arg):
    await ctx.send("gegegege ma'amser")
    rm_input = arg.split(' ')
    rm_input_hour = rm_input[0]
    rm_parsed = ""
    rm_input_arg = rm_input[1:len(rm_input)] 
    for i in rm_input_arg:
        rm_parsed = rm_parsed + " " + str(i)
    rm_input_str = rm_parsed
    rm_tminus = float(rm_input_hour)*3600  
    await asyncio.sleep(rm_tminus)
    await ctx.send("{}, {}".format(ctx.message.author.mention, rm_input_str))

@bot.command()
async def switch(ctx, arg):
    with open(PATH_TO_DIR) as f:
        guild_talkback = dict(filter(None, csv.reader(f)))
    print(guild_talkback)
    id = ctx.message.guild.id
    tb = guild_talkback[str(id)]
    if arg == 'on' and tb == "False":
        guild_talkback[str(id)] = True
        with open(PATH_TO_DIR, 'w') as f:
            for key in guild_talkback.keys():
                f.write("%s,%s\n"%(key,guild_talkback[key]))
        await ctx.send(embed=discord.Embed(title="**[WARNING] MAMA MO MODE: ON**"))
    elif arg == 'off' and tb == "True":
        guild_talkback[str(id)] = False
        with open(PATH_TO_DIR, 'w') as f:
            for key in guild_talkback.keys():
                f.write("%s,%s\n"%(key,guild_talkback[key]))
        await ctx.send(embed=discord.Embed(title='**[WARNING] MAMA MO MODE: OFF**'))
    else:
        await ctx.send('Invalid argument or redundant action. Fucking bobo.')

@bot.event
async def on_message(message):
    ctx = await bot.get_context(message)
    if message.author == bot.user:
        return
    if message.content.startswith(PREFIX):
        await bot.invoke(ctx)
    if "ha" in message.content:
        await message.channel.send('hatdog')
    if "impostor" in message.content:
        if random.randint(1, 100) > 50:
            imp_output = "An"
            imp_count = "1"
            imp_s_1 = ""
            imp_s_2 = "s"
        else:
            imp_output = "not An"
            imp_count = "2"
            imp_s_1 = "s"
            imp_s_2 = ""
        if len(message.raw_mentions) != 0:
            imp_user = '<@'+str(message.raw_mentions[0])+'>'
        else:
            imp_user = message.author.mention
        await message.channel.send("  . 　　　。　　　　•　 　ﾟ　　。 　　." + '\n' + "　.　　　 　　.　　　　　。　　 。　. 　" + '\n' + " .　　 。　　　　　 ඞ 。 . 　　 • 　　　　•" + '\n' + "."+imp_user+ " was "+imp_output+" Impostor.　 。　." + '\n' + "        　　　　   "+imp_count+" Impostor"+imp_s_1+" remain"+imp_s_2+" 　 　　。" + '\n' + "        　　ﾟ　　　.　　　. ,　　　　.　 .. 　　　。　　　　" + '\n' + "        •　 　ﾟ　　。 　　. 　　　。　　　　•　 　ﾟ　　。 ")
    with open(PATH_TO_DIR) as csv_file:
        reader = csv.reader(csv_file)
        guild_talkback = dict(reader)
    id = ctx.message.guild.id
    tb = guild_talkback[str(id)]
    if tb == "True":
        await message.channel.send('mama mo '+message.content)

bot.run(TOKEN)
