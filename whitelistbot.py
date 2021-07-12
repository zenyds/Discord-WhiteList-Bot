import discord
from discord.ext import commands
bot = commands.Bot(command_prefix=['!'], description='A Simple Whitelist Bot') #Here you can change the command prefix and the help message description

wlchannel = #id of the channel where the answers will be sent
prefix = '!'


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('!wl')) #Here you can change the "playing" text for the bot.
    print('Logged in as ' + bot.user.name) #This is a response to the console once the bot is ready.
    print('----------')
    print('Invite URL: ' + 'https://discordapp.com/oauth2/authorize?&client_id=' + str(bot.user.id) + '&scope=bot&permissions=8')
    print('----------')
    print('wl channel id:')
    print(wlchannel)
    print('----------')
    print('bot prefix:')
    print(prefix)
    print('----------')


@bot.command()                 wl info command do this in a wil info channel once then disable the command if you want to
async def wlinfo(ctx):
    emb=discord.Embed(title='Wl info',description='You can make a whitelist application using !wl in any channel.')
    await ctx.channel.send(embed=emb)



@bot.command()     #!wl command will send this to the authors dms
async def wl(ctx):
    emb=discord.Embed(title='"Server Name" WhiteList Applicatiom',description='WhiteList application for "server name" server')
    emb.add_field(name='Question 1',value='Question')
    emb.add_field(name='Question 2',value='Question')
    emb.add_field(name='Question 3',value='Question')
    emb.add_field(name='Question 4',value='Question')
    await ctx.author.send(embed=emb)
    await ctx.message.delete()

@bot.event     #sends the answer to the wl channel
async def on_message(message):
    # Checking if its a dm channel
    if isinstance(message.channel, discord.DMChannel):
        # Getting the channel
        channel = bot.get_channel(wlchannel)
        await channel.send(f"{message.author} sent:\n```{message.content}```")
    # Processing the message so commands will work
    await bot.process_commands(message)

	

bot.run('') #Get your bot token from https://discordapp.com/developers/applications/
