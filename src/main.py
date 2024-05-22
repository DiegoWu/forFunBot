# main.py
# listen messages, reply messages, and process commands

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
# Bot object, command prefix is $
bot = commands.Bot(command_prefix='$')
token = os.getenv("DISCORD_TOKEN")

# read functions from extensions.txt and load them to the bot
with open(os.path.join("..", "info", "extensions.txt"), 'r') as f:
    for extension in f:
        
        
        bot.load_extension(extension.strip('\n')) 

# trigger when bot is ready
@bot.event
async def on_ready():
    print("Ready!")
    # print bot information
    print("User name:", bot.user.name)
    print("User ID:", bot.user.id)

# trigger when message is sent
@bot.event
async def on_message(message):
    # avoid bot to reply itself
    if message.author.id == bot.user.id:
        return

    # reply when user say hello
    if "hello" in message.content.lower():
        await message.channel.send("Hello~ Nice to meet you.") # Bot sends message

    # reply when user ask for help
    if message.content.lower().startswith("help"):
        await message.channel.send("Enter commands starting with $ or enter $help for more information:)")

    # process commands
    await bot.process_commands(message)

# load extension 
# trigger when user type $load
@bot.command(help = "Load extension.", brief = "Load extension.")
async def load(ctx, extension): # extension: the name of the extension
    try:
        bot.load_extension(extension.lower()) # load extension, lower() since the file name is in lower case
        await ctx.send(f"{extension} loaded.") # Bot send message
    except Exception as e:
        await ctx.send(e) # print error message if failed

# unload extension
@bot.command(help = "Un-load extension.", brief = "Un-load extension.")
async def unload(ctx, extension):
    try:
        bot.unload_extension(extension.lower()) 
        await ctx.send(f"{extension} unloaded.") # Bot sends message
    except Exception as e:
        await ctx.send(e)
    

# reload extension
@bot.command(help = "Re-load extension.", brief = "Re-load extension.")
async def reload(ctx, extension):
    try:
        bot.reload_extension(extension.lower()) # load extension, lower() since the file name is in lower case
        await ctx.send(f"{extension} reloaded.") # Bot sends message
    except Exception as e:
        await ctx.send(e) # print error message if failed
    

bot.run(token) # execute bot
