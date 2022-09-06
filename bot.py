import discord
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_perfix='-', intents=intents)

@bot.event
async def on_ready(): # This will display when the bot is online | Letting you know the bot is online
    print(f"-------------------------------------------------------")
    print(f"Logged in as {bot.user.name} | {bot.user.id}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print(f"-------------------------------------------------------")
    

@bot.event
async def on_member_join(member):
    embed=discord.Embed(title="Member | Join!", description=f"", color=0xe700ff) # In Description Put what you want the bot to send!
    embed.set_footer(text="imput footer text", icon_url="input footer icon url")
    embed.set_thumbnail(url=member.avatar)
    await bot.get_channel(welcome channel id).send(embed=embed)
    
@bot.event
async def on_member_remove(member):
    embed=discord.Embed(title="Member | Leave:(", description=f"Sad to See you Leave {member.mention}:(", color=0xe700ff)
    embed.set_footer(text="imput footer text", icon_url="input footer icon url")
    embed.set_thumbnail(url=member.avatar)
    await bot.get_channel(member leave channel id).send(embed=embed)
    
    
bot.run('Input bot Token!')
