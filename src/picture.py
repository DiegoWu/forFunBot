# picture.py
# upload pics, show pics

import discord
from discord.ext import commands
import os
import requests
class Picture(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # upload a picture
    # trigger when user input $upload
    @commands.command(help = "Upload a picture.", brief = "Upload a picture.")
    async def upload(self, ctx):
        # fetch the image from the message
        try:
            response = requests.get(ctx.message.attachments[0].url)
        except IndexError:
            return await ctx.send('Image invalid!')
        # save the image
        file = open(os.path.join("..", "storage", "sample_image.png"), "wb")
        file.write(response.content)
        file.close()

    # bot sends pictures
    # trigger when user input $show_pic
    @commands.command(help = "Show a picture.", brief = "Show a picture.")
    async def show_pic(self, ctx):
        # read the image
        try:
            with open(os.path.join("..", "storage", "sample_image.png"), "rb") as f:
                picture = discord.File(f) # convert the file content to a format that can be sent on discord
                await ctx.send(file = picture) # Bot sends the picture
        except FileNotFoundError:
            await ctx.send('Saved image not found!')

# add the cog to the bot
def setup(bot):
    bot.add_cog(Picture(bot))
